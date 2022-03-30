import shutil

def create_archive(source_directory, destination_name = 'certificate_archive'):
    shutil.make_archive(destination_name, 'zip', source_directory)