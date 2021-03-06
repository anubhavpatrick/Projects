'''A module to upload certificated archieve on Google Drive
Reference - https://www.geeksforgeeks.org/uploading-files-on-google-drive-using-python/

To ensure we do not have reauthenticate ourself repeatedly, we will use the
Reference - https://medium.com/analytics-vidhya/pydrive-to-download-from-google-drive-to-a-remote-machine-14c2d086e84e
'''
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
from pywebio.output import put_markdown
import pathlib
import config

# For using listdir()
import os

def upload_archive(archive_name):
    '''Upload the archive to Google Drive'''

    try:
        # Below code does the authentication
        # part of the code
        gauth = GoogleAuth()

        put_markdown("- Authenticating For Google Drive Access...")

        # Creates local webserver and auto
        # handles authentication.
        #gauth.LocalWebserverAuth()
        gauth.CommandLineAuth()
        drive = GoogleDrive(gauth)

        put_markdown("- Successfully Authenticated...")

        # replace the value of this variable
        # with the absolute path of the directory
        current_dir = os.getcwd()
        f = drive.CreateFile({'title': archive_name})
        f.SetContentFile(os.path.join(current_dir, archive_name))
        f.Upload()

        put_markdown(f'''
        - Certiticate Archive Successfully Uploaded to Google Drive ...
            - Drive Account - **{config.DEFAULT_GOOGLE_DRIVE_ACCOUNT_NAME}**
            - File name: **{archive_name}** ''')

    except Exception as e:
        put_markdown("## !!!Error: "+str(e))

#upload_archive('codewiz_123_archive.zip')
