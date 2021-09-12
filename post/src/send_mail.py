from smtplib import SMTP
import config.config as conf
import base64


def send_mail(message_docx1) -> None:
    """
    Send mail with actually data of weather in Saint-Petersburg
    :param message_docx1: html file with parameters of weather
    """
    server = SMTP(conf.smtp_server, conf.smtp_port)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(base64.b64decode(conf.server_mail).decode('utf-8'),
                 base64.b64decode(conf.password_mail).decode('utf-8'))

    subject = conf.topic
    body = message_docx1

    message = conf.message % (subject, body)

    server.sendmail(
        base64.b64decode(conf.server_mail).decode('utf-8'),
        conf.sender_mail,
        message

    )
    server.quit()
