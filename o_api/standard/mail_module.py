import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

port = 587
smtp_server = 'smtp.gmail.com'
sender_email = 'qnsekddl1@gmail.com'
receiver_email = 'qnsekddl1@gmail.com'
password = 'zkfk swkx tgri xmsv'
message = "<h1>반가워</h1>"

msg = MIMEText(message, 'html')
data = MIMEMultipart()
data.attach(msg)
context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, data.as_string("utf-8"))