import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from datetime import datetime

def enviar_email():
    remetente = os.environ['GMAIL_USER']
    senha = os.environ['GMAIL_APP_PASSWORD']
    destinatario = "isaacsonecamcbaby@gmail.com"
    
    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = f"Palpites do Dia - {datetime.now().strftime('%d/%m/%Y')}"
    
    corpo = """
    Aqui vão os palpites de hoje:
    
    1. Real Madrid x Barcelona - Mais de 2.5 gols
    2. Manchester City x Arsenal - Ambas marcam
    3. Bayern x Dortmund - Vitória do Bayern
    
    Boa sorte!
    """
    
    msg.attach(MIMEText(corpo, 'plain'))
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(remetente, senha)
    server.send_message(msg)
    server.quit()
    print("Email enviado!")

if __name__ == "__main__":
    enviar_email()
