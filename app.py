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

        base64_string = request.form['InputImgFromCanvas']
        base64_string = str.replace(base64_string, "data:image/png;base64,",
                                    "")
        base64_string = str.replace(base64_string, " ", "+")

        # Adding Padding
        missing_padding_length = len(base64_string) % 4
        if missing_padding_length != 0:
            base64_string = base64_string + '=' * (4 - missing_padding_length)

        decoded_data = base64.b64decode(base64_string)
        output_file_name = generateuniquefilename('png')
        writefile(decoded_data, output_file_name)

        senderemail = request.form['senderEmail']
        print(senderemail)
        recipientemail = request.form['recipientEmail']
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
    #emailstatusmsg= 'Email failed'
    #return render_template('index.html')


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

        # Send the message via local SMTP server.
    try:
        #todo Extenalize server name, port number
        sendingemail = smtplib.SMTP("localhost", 2500)
        #todo if(SMTP.AUTH.REQUIRED == TRUE)
        #         #sendingemail.login([SMTP.USER.NAME], [SMTP.PWD])
        print(senderemail, recipientemail)
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
