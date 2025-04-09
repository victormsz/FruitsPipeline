import os
import smtplib
from email.mime.text import MIMEText

dest_email = os.getenv("DEST_EMAIL", "default@example.com")

msg = MIMEText("Pipeline executado com sucesso!")
msg['Subject'] = 'CI/CD Notification'
msg['From'] = 'victormsz09@yahoo.com.br'
msg['To'] = dest_email

with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login(os.getenv("SMTP_USER"), os.getenv("SMTP_PASS"))
    server.send_message(msg)