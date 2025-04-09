import os
import smtplib
from email.mime.text import MIMEText

# Pega variáveis do ambiente
email_destino = os.environ.get("EMAIL_AUTOR")
smtp_user = os.environ.get("SMTP_USER")
smtp_pass = os.environ.get("SMTP_PASS")
email_remetente = smtp_user  # usa o mesmo que faz o login

# Validação básica
if not all([email_destino, smtp_user, smtp_pass]):
    raise EnvironmentError("Variáveis de ambiente obrigatórias não definidas.")

# Monta a mensagem
msg = MIMEText("Pipeline executado com sucesso!")
msg['Subject'] = 'CI/CD Notification'
msg['From'] = email_remetente
msg['To'] = email_destino

# Envia o e-mail
with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login(smtp_user, smtp_pass)
    server.send_message(msg)