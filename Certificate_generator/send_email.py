'''This modules sends emails using the gmail SMTP server.
Reference - https://www.geeksforgeeks.org/send-mail-attachment-gmail-account-using-python/

For allowing gmail to send emails, you need to enable less secure apps in your gmail account.
Reference -https://support.google.com/accounts/answer/6010255?hl=en#zippy=%2Cif-less-secure-app-access-is-on-for-your-account
'''

# Python code to illustrate Sending mail with attachments
# from your Gmail account

# libraries to be imported
from getpass import getpass
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = "anubhav.patrick@kiet.edu"
toaddr = "anubhavpatrick@gmail.com"

# instance of MIMEMultipart
msg = MIMEMultipart()

# storing the senders email address
msg['From'] = fromaddr

# storing the receivers email address
msg['To'] = toaddr

# storing the subject
msg['Subject'] = "Test Mail 2"

# string to store the body of the mail
body = "This is second test mail to check the gmail SMTP server"

# attach the body with the msg instance
msg.attach(MIMEText(body, 'plain'))

# open the file to be sent
filename = "certificate.png"
attachment = open(filename, "rb")

# instance of MIMEBase and named as p
p = MIMEBase('application', 'octet-stream')

# To change the payload into encoded form
p.set_payload((attachment).read())

# encode into base64
encoders.encode_base64(p)

p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

# attach the instance 'p' to instance 'msg'
msg.attach(p)

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
#read password from console
password = getpass("Enter your password: ")
s.login(fromaddr, password)

# Converts the Multipart msg into a string
text = msg.as_string()

# sending the mail
s.sendmail(fromaddr, toaddr, text)

# terminating the session
s.quit()


