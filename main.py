import os
import smtplib
from email.message import EmailMessage

# email credentials
EMAIL_ADDRESS = 'emaildeenvio@teste.com.br'
EMAIL_PASSWORD = 'password'
EMAIL_SMTP = 'smtp.gmail.com'
EMAIL_PORT = 465

# mounting email
msg = EmailMessage()
msg['Subject'] = 'title'
msg['From'] = 'emaildeenvio@teste.com.br'
msg['To'] = 'destinatario@teste.com.br'
msg.set_content('Email de Teste, não responder')

# send email
with smtplib.SMTP_SSL(EMAIL_SMTP, EMAIL_PORT) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
