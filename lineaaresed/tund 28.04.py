# https://myaccount.google.com/apppasswords Rakenduste paroolid
import smtplib, ssl
from email.message import EmailMessage

def saada_kiri():
    kellele = input("Kellele: ")
    kellolt = "Tere, see on test"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    kellolt = "anastasiamayba@gmail.com"
    parool = input("Rakenduste parool: ")
    context = ssl.create_default_context()
    msg = EmailMessage()
    msg['Subject'] = "Test"
    msg['From'] = kellolt
    msg['To'] = kellele

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls(context=context)
        server.login(kellolt, parool)
        server.send_message(msg)
        print("Kiri saadetud")
    except Exception as e:
        print("Viga:", e)
