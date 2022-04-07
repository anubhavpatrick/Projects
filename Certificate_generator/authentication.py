'''
This module provides password authentication for the application
'''

def simple_matcher(pwd):
    '''A function to match the password'''
    if pwd == 'cpp123':
        return True
    else:
        return False

#TODO - Add a function to check if the password is correct
