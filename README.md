### POSTCARD CREATOR WEB APPLICATION

This is a simple web application being developed with Flask/Python framework which is intented for creating Postcard online and email it as an attachment.

## PREREQUISITIES

1. Python3.6
2. Flask Framework
3. SMTP Server

## INSTALLATIONS
# 1. Python 

- Go to https://www.python.org/downloads/ and download the latest version available for your machine.
- Run the downloaded file and install the python 3.6
- set the ENVIRONMENT PATH VARIABLE to the scripts folder of python installed
(windows->Control Panel->Advanced system settings->Environment Variable->set the path attribute)

# 2. Flask

- Navigate to the python installed folder (example-> C:\Users\<<Your Folder>>\AppData\Local\Programs\Python\Python36\scripts in windows)
- Inside the scripts folder, execute in command prompt as 
         >>>pip3.6 install flask

# 3. SMTP Server

- Need SMTP Server for the email communication. Need the server name, port and its credentials(username, password).


## HOW TO EXECUTE THE APPLICATION

- Download from github url https://github.com/AshwiniSaran/Postcard_Creator 

- In order to include ther SMTP Server to the program
    - Navigate to Application folder and open app.py
    - Assign the available SMPT Server Name, port and credentials respectively in app.py as shown below
    - Save and close app.py
                  
                  #Provide SMTP Server Name
                  SMTP_SERVER_NAME = " "   #localhost"
                  #Provide SMTP Port
                  SMPT_SERVER_PORT = " "   #2500"

                  #Provide SMTP Credentials
                  SMTP_USER_NAME = ""
                  SMTP_USER_PWD = ""

                  
   
- Open the command prompt and navigate to the application file folder
    - In windows run as >python app.py
    - In Linux change the script as executable using chmod+x and then run as python app.py
        
- Open http://localhost:5000 in the browser so that the application is available. 
