'''
A module that tracks the details of certificates created
'''

#import logging

def certificate_details_logger(log_str:str):
    '''A function to create a logger for certificate details'''
    
    #Issue - Python inbuilt logging module not working
    #The reason may be because of server may be writing its own logs
    #logging.basicConfig(filename='certificate_generated.log', encoding='utf-8', level=logging.DEBUG, force=True)
    #logging.info(log_str)
    
    #Alternate option - Use simple file handling
    with open('certificate_generated.log', 'a') as f:
        f.write(log_str)



