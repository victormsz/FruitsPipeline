import os
import smtplib
from email.mime.text import MIMEText

email = os.environ.get("EMAIL_AUTOR")

msg = MIMEText("Pipeline executado com sucesso!")
msg['Subject'] = 'CI/CD Notification'
msg['From'] = 'victormsz09@yahoo.com.br'
msg['To'] = email

with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login(os.getenv("SMTP_USER"), os.getenv("SMTP_PASS"))
    server.send_message(msg)


