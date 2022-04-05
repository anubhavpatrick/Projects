'''
GUI for the user to input parameters for certificate generation

Reference - https://pywebio.readthedocs.io/en/latest/
'''

from pywebio.input import input, radio,input_group,file_upload
from pywebio.output import put_text, put_file, put_markdown
from pywebio import start_server
import generator_script
import create_certificate_archive
import upload_certificate_archive
import os

def main_GUI():
    '''Create GUI for the user to input parameters for certificate generation and call the supporting functions'''

    info = input_group("Give Details For Certificate Generation",[
    input("Give name of the event", placeholder= "CODEWIZ 1.0",name = "event_name", value="CODEWIZ 1.0"),
    input("Give name of the session", placeholder= "2021-22", name = "session",value="2021-22"),
    file_upload(label="Upload (.png) template", accept = ".png", placeholder= "If not selected, a default template will be selected from the project directory", name = "template_file"),
    file_upload(label="Upload (.xlsx) result file in SNo, Section Name, Roll No, Email, Score format", accept = ".xlsx", placeholder= "By default, the results.xlsx will be selected from the project directory", name = "result_file"),
    radio("Do you want to upload the zip archive to Google Drive", options=["Yes", "No"], name = "upload_require", value = "No"),
    radio("Do you want to also send the emails with attached certificate to the participants [Use with caution]", options=["Yes", "No"], name = "email_require", value = "No")
    ] , cancelable=True
    )

    try:
        #call the necessary functions based on user input
        put_markdown("# Thank you for using the Certificate Generator")

        put_markdown("### *Made with ❤️ by [Anubhav Patrick](https://www.linkedin.com/in/anubhavpatrick/)* ")

        put_markdown("- Creating Certificates...")
        
        #saving the result file in the project directory
        if info["result_file"] is None:
            #if the user does not upload the result file, then the default result file will be used
            result_file_name = "results.xlsx"
        else:
            os.makedirs("assets/", exist_ok=True)
            open('assets/results.xlsx', 'wb').write(info["result_file"]['content'])
            result_file_name = "assets/results.xlsx" 

        #saving the template file in the project directory
        if info["template_file"] is None:
            #if the user does not upload the template file, then the default result file will be used
            template_file_name = "certificate.png"
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
        if info['upload_require'] == "Yes":
            upload_certificate_archive.upload_archive(archive_name)
        elif info['email_require'] == "Yes":
            pass
            #create_certificate_archive.create_archive(event_name_formatted, event_name_formatted+'_archive')
        put_markdown("- Certificates Successfully Generated")
        # read the certificate archive content and give option to download it
        content = open(archive_name, 'rb').read() 
        put_file(archive_name, content, 'Download Certificate Archive')
    
    except Exception as e:
        put_markdown("## !!!Error in generating certificates")
        put_text(e)


if __name__ == '__main__':

    #main_GUI()
    start_server(main_GUI, host='',remote_access=True)