import smtplib
from email.message import EmailMessage

#Server connection
smtp_server = smtplib.SMTP('smtp.yandex.ru', 587)
smtp_server.starttls()
username = 'stasrusov2003'
password = 'acdc2003-FNS'
smtp_server.login(username, password)


# Создание объекта письма
msg = EmailMessage()
msg['Subject'] = 'Привет!'
msg['From'] = 'stasrusov2003@yandex.ru'
msg['To'] = 'lutsenko.anton1990@gmail.com'
msg.set_content('Содержимое текста письма.')


smtp_server.send_message(msg)

smtp_server.quit()