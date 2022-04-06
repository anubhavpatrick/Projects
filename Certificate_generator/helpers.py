'''A module containing helper functions for the Certificate Generator'''
from tkinter import E
import openpyxl
import os

#Reference -https://www.geeksforgeeks.org/python-print-initials-name-last-name-full/
def abbreviated_name(s):
    '''python program to print initials of a name '''

    # split the string into a list 
    l = s.split()
    new = ""
  
    # traverse in the list 
    for i in range(len(l)-1):
        s = l[i]
          
        # adds the capital first character 
        new += (s[0].upper()+'.')
          
    # l[-1] gives last item of list l. We
    # use title to print first character in
    # capital.
    new += l[-1].title()
      
    return new 

def number_of_certificates(result_file_name):
    ''' loading the details.xlsx workbook
     and grabbing the active sheet'''
    obj = openpyxl.load_workbook(result_file_name)
    sheet = obj.active 
    return sheet.max_row-1

def hard_cleanup():
    '''Use with caution. Action is irreplacable
    Remove all the certificate related files in the current directory
    and the directory itself'''

    try:
        #delete certificate directories
        with open('certificate_generated.log', 'r') as f:
            lines = f.readlines()
            for line in lines:
                line_seperated = line.split(':')
                if line_seperated[0] == 'Event Name':
                    event_name = line_seperated[1].strip()
                    print(event_name)
                    os.system('rm -rf ' + event_name)
        #remove all the certificate zip files in the current directory
        for file in os.listdir():
            if file.endswith('.zip'):
                os.remove(file)
    except Exception as e:
        print(e)

#Uncomment to delete files and directories of all previously generated certificates
#hard_cleanup()