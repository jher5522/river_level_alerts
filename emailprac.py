# THIS WORKS!
#from the first line of http://stackoverflow.com/questions/11445523/python-smtplib-is-sending-mail-via-gmail-using-oauth2-possible
import os

def sendmail(to, message, subject):
    import smtplib

    gmail_user = 'herbertjemma@gmail.com'
    pwdPath=os.path.abspath('..')+'\\emailConfig.txt'
    f=open(pwdPath)
    gmail_pwd = f.read()
    smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(gmail_user, gmail_pwd)
    header = 'To:' + ', '.join(to) + '\n' + 'From: ' + gmail_user + '\n' + 'Subject: ' + subject +  '\n'
    print header
    msg = header + message + '\n'
    smtpserver.sendmail(gmail_user, to, msg)
    print 'done!'
    smtpserver.close();
