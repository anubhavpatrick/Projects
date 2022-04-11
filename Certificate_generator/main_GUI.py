# -*- coding: utf-8 -*-

'''
GUI for the user to input parameters for certificate generation

Reference - https://pywebio.readthedocs.io/en/latest/
'''

from pywebio.input import input, radio,input_group,file_upload,PASSWORD
from pywebio.output import put_text, put_file, put_markdown
from pywebio import start_server
from pywebio import session
import generator_script
import create_certificate_archive
import upload_certificate_archive
import certificate_generated_log
from helpers import create_log_entry
import os
import config
import send_email
import authentication

def main_GUI():
    '''Create GUI for the user to input parameters for certificate generation and call the supporting functions'''

    #Headers for the GUI
    put_markdown("# Welcome to the Certificate Generator v3.1")
    put_markdown("### *Made with ❤️ by [Anubhav Patrick](https://www.linkedin.com/in/anubhavpatrick/)*")

    #Password authentication
    pwd = input('Enter app password: ', type=PASSWORD)
    if authentication.verify_password(pwd):
        info = input_group("Give Details For Certificate Generation",[
        input("Give name of the event", placeholder= config.DEFAULT_EVENT_NAME,name = "event_name", value=config.DEFAULT_EVENT_NAME),
        input("Give name of the session", placeholder= config.DEFAULT_SESSION, name = "session",value=config.DEFAULT_SESSION),
        file_upload(label="Upload (.png) template", accept = ".png", placeholder= "If not selected, a default template will be selected from the project directory", name = "template_file"),
        file_upload(label="Upload (.xlsx) result file in |SNo|Section Name|Roll No|Email|Score| format", accept = ".xlsx", placeholder= "By default, the results.xlsx will be selected from the project directory", name = "result_file"),
        radio(f"Upload the zip archive to Google Drive\n[Account: {config.DEFAULT_GOOGLE_DRIVE_ACCOUNT_NAME}]", options=["Yes", "No"], name = "upload_require", value = "No"),
        radio(f"Send the emails with attached certificate to the participants\n[Account: {config.DEFAULT_SENDER_EMAIL}]", options=["Yes", "No"], name = "email_require", value = "No")
        ] , cancelable=True
        )

        try:
            #call the necessary functions based on user input
            put_markdown("- Generating Certificates...")
            
            #saving the result file in the project directory
            if info["result_file"] is None:
                #if the user does not upload the result file, then the default result file will be used
                result_file_name = config.DEFAULT_RESULT_FILE
            else:
                os.makedirs("assets/", exist_ok=True)
                open('assets/results.xlsx', 'wb').write(info["result_file"]['content'])
                result_file_name = "assets/results.xlsx" 

            #saving the template file in the project directory
            if info["template_file"] is None:
                #if the user does not upload the template file, then the default result file will be used
                template_file_name = config.DEFAULT_TEMPLATE_FILE
            else:
                os.makedirs("assets/", exist_ok=True)
                open('assets/certificate.png', 'wb').write(info["template_file"]['content'])
                template_file_name = "assets/certificate.png"
                            
            generator_script.generate_certificate(result_file_name, template_file_name, info['session'], info['event_name'])
            #provide a name to the archive
            event_name_formatted = info['event_name'].strip().lower().replace(' ','_').replace('.','_')
            #Archiving the certificate files
            archive_name = event_name_formatted+'_archive.zip'
            create_certificate_archive.create_archive(event_name_formatted, event_name_formatted+'_archive')
            put_markdown("- Certificates Successfully Generated")

            if info['upload_require'] == "Yes":
                upload_certificate_archive.upload_archive(archive_name)
            
            if info['email_require'] == "Yes":
                send_email.prepare_email(info['event_name'], result_file_name)
                put_markdown("- Emails Successfully Sent")
                
            #create_certificate_archive.create_archive(event_name_formatted, event_name_formatted+'_archive')

            # read the certificate archive content and give option to download it
            content = open(archive_name, 'rb').read() 
            put_file(archive_name, content, 'Download Certificate Archive To Local Machine')

            #adding details of the certificates generated to the log file
            certificate_generated_log.certificate_details_logger(create_log_entry(event_name_formatted, 
                                                                info['session'], 
                                                                template_file_name, 
                                                                result_file_name,
                                                                info['upload_require'],
                                                                info['email_require'] ))

            #ensuring the session is not closed
            session.hold()
        
        except Exception as e:
            put_markdown("## !!!Error in generating certificates")
            put_text(e)
    
    else:
        put_markdown("## !!!Wrong Password")


if __name__ == '__main__':

    #main_GUI()
    start_server(main_GUI, host='',remote_access=True, reconnect_timeout=1000, max_payload_size='1000M', websocket_ping_interval=50)#, websocket_ping_timeout=5000)