import smtplib
from email.message import EmailMessage

def send_email(to,content):
    msg=EmailMessage()
    msg.set_content(content)
    msg['Subject']='Automation Report'
    msg['From']='your@gmail.com'
    msg['To']=to
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as s:
        s.login('your@gmail.com','app_password')
        s.send_message(msg)
