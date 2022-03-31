'''
GUI for the user to input parameters for certificate generation

Reference - https://pywebio.readthedocs.io/en/latest/
'''

from pywebio.input import input, radio,input_group
from pywebio.output import put_text
import generator_script
import create_certificate_archive
import upload_certificate_archive
import os

def main_GUI():
    '''Create GUI for the user to input parameters for certificate generation and call the supporting functions'''

    info = input_group("Give Details For Certificate Generation",[
    input("Give name of the event", placeholder= "CODEWIZ 1.0",name = "event_name", value="CODEWIZ 1.0"),
    input("Give name of the session", placeholder= "2021-22", name = "session",value="2021-22"),
    input("Give the path of the template", placeholder= "certificate.png", name = "template_path", value = "certificate.png"),
    input("Give the path with the result file name of participants in xlsx format. The columns of result file must be SNo, Section, Class_Roll_Num, Name, Email", placeholder= "results.xlsx", name = "result_file", value = "results.xlsx"),
    radio("Do you want to create a zip archive", options=["Yes", "No"],name = "zip_require",value = "No"),
    radio("Do you want to upload the zip archive to Google Drive", options=["Yes", "No"],upload_require = "Yes", name = "upload_require", value = "No")
    ] )

    try:

        #call the necessary functions based on user input
        generator_script.generate_certificate(info['result_file'], info['template_path'], info['session'], info['event_name'])
        event_name_formatted = info['event_name'].strip().lower().replace(' ','_').replace('.','_')
        if info['zip_require'] == "Yes":
            create_certificate_archive.create_archive(event_name_formatted, event_name_formatted+'_archive')
        if info['upload_require'] == "Yes":
            dir = os.listdir()
            archive_name = event_name_formatted+'_archive.zip'
            if archive_name not in dir:
                create_certificate_archive.create_archive(event_name_formatted, event_name_formatted+'_archive')
            upload_certificate_archive.upload_archive(archive_name)
        put_text("Certificates Generated")
    except:
        put_text("Error in generating certificates")


if __name__ == '__main__':
    main_GUI()