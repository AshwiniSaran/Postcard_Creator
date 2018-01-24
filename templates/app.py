#!usr/bin/python
""" Post Card APP"""

import smtplib
import os
import time

import base64
from datetime import datetime

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

from flask import Flask, render_template, request

APP = Flask(__name__)
APP.config['TEMPLATES_AUTO_RELOAD'] = True

#Provide SMTP Server Name
SMTP_SERVER_NAME = ""   #localhost"
#Provide SMTP Port
SMPT_SERVER_PORT = ""   #2500"

#set SMTP_AUTH_REQUIRED as 1
SMTP_AUTH_REQUIRED = 0

#Provide SMTP Credentials
SMTP_USER_NAME = ""
SMTP_USER_PWD = ""

@APP.route('/')
def homepage():
    """ Renders Homepage"""
    try:
        result = ""
        return render_template('index.html', result=result)
    except Exception as ex:
        print(ex)
        return render_template('index.html')


@APP.route('/uploaddata', methods=['POST'])
def uploaddata():
    """ Uploads data to the server from client """
    try:
        #Read canvas data
        base64_string = request.form['InputImgFromCanvas']
        base64_string = str.replace(base64_string, "data:image/png;base64,", "")
        base64_string = str.replace(base64_string, " ", "+")

        missing_padding_length = len(base64_string) % 4
        if missing_padding_length != 0:
            base64_string = base64_string + '=' * (4 - missing_padding_length)

        decoded_data = base64.b64decode(base64_string)
        output_file_name = generateuniquefilename('png')
        writefile(decoded_data, output_file_name)

        senderemail = request.form['senderEmail']
        recipientemail = request.form['recipientEmail']
        #invoke emailing function
        emailstatus = send_email(senderemail, recipientemail, output_file_name)
        if emailstatus == 1:
            result = "Email sent successfully"
            print(result)
            return render_template('index.html', result=result)
        else:
            result = "Email failed"
            print(result)
            return render_template('index.html', result=result)
    except Exception as ex:
        result = ex
        print(result)
        return render_template('index.html', result=result)

def send_email(senderemail, recipientemail, imgfilename):
    """sends email"""
    # print('entering send_email()')
    msgroot = MIMEMultipart('related')
    msgroot['Subject'] = "Postcard For You!!"
    msgroot['From'] = senderemail
    msgroot['To'] = recipientemail
    msgroot['Date'] = str(datetime.now())
    msgroot['Sent Date'] = str(datetime.now())
    # Create the body of the message.
    html = """\
            <p>Have a nice day!!</p>
         """
    # Record the MIME types.
    msghtml = MIMEText(html, 'html')
    if imgfilename is not False:
        img_fp = open(imgfilename, 'rb')
        msgimg = MIMEImage(img_fp.read())
        img_fp.close()
        #  msgimg.add_header('Content-ID', '<imagetag>')
        msgimg.add_header(
            'Content-Disposition',
            'attachment',
            filename='postcard' + str(datetime.now()) + '.png')
        msgroot.attach(msghtml)
        msgroot.attach(msgimg)
    try:
        #sendingemail = smtplib.SMTP("localhost", 2500)
        sendingemail = smtplib.SMTP(SMTP_SERVER_NAME, SMPT_SERVER_PORT)
        #todo if(SMTP.AUTH.REQUIRED == TRUE)
        if  SMTP_AUTH_REQUIRED == 1:
            sendingemail.login(SMTP_USER_NAME, SMTP_USER_PWD)
        else:
            print("Invalid SMTP credentails")
            return 0
        print('from'+senderemail+' to'+recipientemail)
        sendingemail.sendmail(senderemail, recipientemail, msgroot.as_string())
        sendingemail.quit()
        return 1
    except Exception as ex:
        print(ex)
        return 0


def readfile(filename):
    """reads a file"""
    file_object = open(filename, 'r')
    read_data = file_object.read()
    print(read_data)
    file_object.close()
    return read_data


def writefile(content, filename):
    """Writes a file with the given name and the given text."""
    output = open(filename, "wb")
    output.write(content)
    output.close()


def generateuniquefilename(extn):
    """Generates Img Attachment name"""
    current_time = time.time()
    time_stamp = datetime.fromtimestamp(current_time).strftime(
        '%Y_%m_%d_%H_%M_%S')
    output_file_name = os.getcwd(
    ) + "/output/" + "postcard" + time_stamp + "." + extn
    return output_file_name

if __name__ == "__main__":
    APP.run()
