''' A module to parse command line arguments
Reference - https://pythonprogramming.net/argparse-cli-intermediate-python-tutorial/
'''

import argparse
from ast import arg
import generator_script
import os
import create_certificate_archive
import upload_certificate_archive
def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', type = str, default = 'results.xlsx', help = 'Give the path with the result file name of participants in xlsx format. The columns of result file must be SNo, Section, Class_Roll_Num, Name, Email')
    parser.add_argument('-t', type = str, default = 'certificate.png', help ='Give the path with file name of certificate template')
    parser.add_argument('-s', type = str, default = '2021-22', help ='Give the session of the certificate')
    parser.add_argument('-n', type = str, default = 'CODEWIZ 1.0', help ='Give the name of the event')
    parser.add_argument('-z', action='store_true', help ='Use this flag if you want to create a zip archive')
    parser.add_argument('-u', action='store_true', help ='Use this flag if you want to upload the zip archive to Google Drive')
    args = parser.parse_args()
    return (args.i, args.t, args.s, args.n,args.z,args.u)

if __name__ == '__main__':
    result_file, template_path, session, event_name, zip_require, upload_require = arg_parser()
    generator_script.generate_certificate(result_file, template_path, session, event_name)
    event_name_formatted = event_name.strip().lower().replace(' ','_').replace('.','_')
    if zip_require:
        create_certificate_archive.create_archive(event_name_formatted, event_name_formatted+'_archive')
    if upload_require:
        dir = os.listdir()
        archive_name = event_name_formatted+'_archive.zip'
        if archive_name not in dir:
             create_certificate_archive.create_archive(event_name_formatted, event_name_formatted+'_archive')
        upload_certificate_archive.upload_archive(archive_name)