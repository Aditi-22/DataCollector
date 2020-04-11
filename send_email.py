from email.mime.text import MIMEText
import smtplib

def send_email(email,height,avg_height,count):
    from_email="aditikansal05@gmail.com"
    from_password="Gemail_1901"
    to_email=email
    subject = "Height Data"
    message = "Hey there, your height is: <strong>%s</strong>. <br> Average height of all is <strong>%s</strong> and that is calculated out of <strong>%s</strong> people. Thanks!!" % (height,avg_height,count) 

    msg = MIMEText(message,'html')
    msg['Subject']=subject
    msg['From']= from_email
    msg['To'] = to_email
    gmail =  smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email,from_password)
    gmail.send_message(msg)
