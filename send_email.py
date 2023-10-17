import smtplib
from email.message import EmailMessage
from Item import *
import re



def send_email_successful_buying(to_email,item):
    if not is_valid_email(to_email):
        raise ValueError('Not a valid email')
    if not isinstance(item,Item):
        raise ValueError('Not an item')

    email = EmailMessage()
    email['from'] = 'My store'
    email['to'] = to_email
    email['subject'] = 'Thanks for shopping with us!'

    email.set_content(f'Transaction has been made successfully.\n'
                      f'Item - {item.name}\n'
                      f'Price - {item.price}$\n'
                      f'Come visit us again!\n')

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('idoebay4567@gmail.com', 'uewrbrelufcyqjzx')
        smtp.send_message(email)
        print('Email has been sent successfully!')


def is_valid_email(email):
    pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.com$)")
    return pattern.match(email)