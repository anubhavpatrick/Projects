'''
This module provides password authentication for the application
Reference - https://passlib.readthedocs.io/en/stable/
'''

import pickle
from passlib.hash import pbkdf2_sha256

def store_password(pwd, file='password.p'):
    '''A function to store the password'''
    pwd_hash = pbkdf2_sha256.hash(pwd)
    with open('password.p', 'wb') as f:
        pickle.dump(pwd_hash, f)

def verify_password(pwd, file='password.p'):
    '''A function to verify the password'''
    with open(file, 'rb') as f:
        pwd_hash = pickle.load(f)
    return pbkdf2_sha256.verify(pwd, pwd_hash)

def simple_matcher(pwd):
    '''A function to match the password'''
    if pwd == 'cpp123':
        return True
    else:
        return False

