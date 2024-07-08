import smtplib
import ssl


def send_mail(message):
    host = "smtp.gmail.com"
    port = 465

    username = "indulahari6@gmail.com"
    password = ""

    receiver = "indulahari6@gmail.com"

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context)as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)