import smtplib
from email.message import EmailMessage
from tkinter import *

def send_email():
    sender_email = 'teplyakova.teplyakova.na@ya.ru'
    recipient_mail = 'tepliakov.ilia@ya.ru'
    password = 'pjhyjmthmbxodafb'
    subject = 'Проверка связи!'
    body = 'Привет из программы на Питоне!'

    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_mail

    server = None

    try:
        server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
        server.login(sender_email, password)
        server.send_message(msg)
        print('Письмо отправлено')
    except Exception as e:
        print(f'Ошибка: {e}')

    finally:
        if server:
            server.quit()

window = Tk()
window.title("Отправка Email")
window.geometry('500x300')

Label(text="Отправитель:").grid(row=0, column=0, sticky=w)
sender_email_entry = Entry()
sender_email_entry.grid(row=0, column=1, sticky=w)

Label(text="Получатель:").grid(row=1, column=0, sticky=w)
recipient_email_entry = Entry()
recipient_email_entry.grid(row=1, column=1, sticky=w)

Label(text="Пароль приложения:").grid(row=2, column=0, sticky=w)
password_entry = Entry()
password_entry.grid(row=2, column=1, sticky=w)

Label(text="Тема письма:").grid(row=3, column=0, sticky=w)
subject_entry = Entry()
subject.grid(row=3, column=1, sticky=w)

Label(text="Сообщение:").grid(row=4, column=0, sticky=w)
body_text = Text(width=45, height=10)
body_text.grid(row=4, column=1, sticky=w)

Button(text="Отправить письмо", command = send_email).grid(row=5, column=1, sticky=w)

result_label = Label(text="")
result_label.grid(row=6, column=1, sticky=w)

window.mainloop()