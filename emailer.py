import smtplib, ssl
from email.mime.text import MIMEText
from config import config

def send_email(content):
    msg = MIMEText(content)
    msg['Subject'] = "🔔 Token Recomendado del Momento"
    msg['From'] = config['email_sender']
    msg['To'] = config['email_recipient']

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(config['smtp_server'], config['smtp_port'], context=context) as server:
        server.login(config['email_sender'], config['email_password'])
        server.send_message(msg)
