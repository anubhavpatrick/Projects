'''A module to upload certificated archieve on Google Drive
Reference - https://www.geeksforgeeks.org/uploading-files-on-google-drive-using-python/
'''
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
from pywebio.output import put_text
import pathlib

# For using listdir()
import os

def upload_archive(archive_name):
    '''Upload the archive to Google Drive'''

    try:
        # Below code does the authentication
        # part of the code
        gauth = GoogleAuth()

        put_text("Authenticating...")

        # Creates local webserver and auto
        # handles authentication.
        gauth.LocalWebserverAuth()	
        drive = GoogleDrive(gauth)

        # replace the value of this variable
        # with the absolute path of the directory
        current_dir = os.getcwd()
        f = drive.CreateFile({'title': archive_name})
        f.SetContentFile(os.path.join(current_dir, archive_name))
        f.Upload()

        '''
        # iterating thought all the files/folder
        # of the desired directory
        for x in os.listdir(path):

            f = drive.CreateFile({'title': x})
            f.SetContentFile(os.path.join(path, x))
            f.Upload()

            # Due to a known bug in pydrive if we
            # don't empty the variable used to
            # upload the files to Google Drive the
            # file stays open in memory and causes a
            # memory leak, therefore preventing its
            # deletion
            f = None
        '''
    except Exception as e:
        put_text("Error: "+str(e))
