from codecs import open
from email.mime.text import MIMEText
from time import sleep
from datetime import datetime
import send_mail
import config.config as conf

# Unpacking the html file to read and work with it
message_docx1 = MIMEText(open(conf.path_file, 'r', encoding='utf-8').read(), 'html', 'utf-8')

# Infinity cycle for working program
while True:
    current_date_time = datetime.now()
    current_time = current_date_time.time()
    # Send message in the morning
    if (str(datetime.now())[11:-7]) == conf.time_morning:
        send_mail.send_mail(message_docx1)
        sleep(3)
    # Send message in the evening
    if (str(datetime.now())[11:-7]) == conf.time_evening:
        send_mail.send_mail(message_docx1)
        sleep(3)
