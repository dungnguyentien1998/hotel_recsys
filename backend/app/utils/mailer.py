import os
import logging
from django.conf import settings
from emails import Message
from emails.template import JinjaTemplate
from app.utils.security import TokenType, generate_token
import yagmail


# Send email function, with parameters subject, html, environment and received email
# def send_mail(mail_to, subject, html, environment):
#     if environment is None:
#         environment = {}
#
#     # Create message
#     message = Message(subject=JinjaTemplate(subject),
#                       html=JinjaTemplate(html),
#                       mail_from=(settings.EMAIL_FROM_NAME, settings.EMAIL_FROM_EMAIL))
#     # Setting host, port, tls, user, password
#     smtp_options = {'host': settings.SMTP_HOST, 'port': settings.SMTP_PORT}
#     if settings.SMTP_TLS:
#         smtp_options['tls'] = True
#     if settings.SMTP_USER:
#         smtp_options['user'] = 'hotelrecsys.no.reply@gmail.com'
#     if settings.SMTP_PASSWORD:
#         smtp_options['password'] = '2EBpSdO8AgMp99QU'
#
#     # Receive response after send email
#     response = message.send(mail_from='dung.nguyentien1998@gmail.com', to=mail_to, render=environment, smtp=smtp_options)
#     logging.info(f'Send email result: {response}')


# Send email for new account
def send_new_account_email(user):
    receiver = user.email
    token = generate_token(obj=user.uuid, _type=TokenType.NEW_ACCOUNT)
    body = "Token to activate account: " + token
    # link = "http://localhost:8000/api/activate?token=" + token + "&email=" + receiver
    # body = "<form id='test' method='post' action='" + link + "'>" \
    #        + "<a href='javascript:;' onclick='document.getElementById('test').submit();'>Activate</a>" + "</form>"
    yag = yagmail.SMTP(user='dung.nguyentien1998@gmail.com', password='Tiendung1098')
    yag.send(
        to=receiver,
        subject="New account",
        contents=body
    )


# Send email for new account
def send_forgot_password(user):
    receiver = user.email
    token = generate_token(obj=user.uuid, _type=TokenType.FORGOT_PASSWORD)
    body = "Token to reset password: " + token
    yag = yagmail.SMTP(user='dung.nguyentien1998@gmail.com', password='Tiendung1098')
    yag.send(
        to=receiver,
        subject="Forgot password",
        contents=body
    )


def send_booking_notification_to_user(user, booking):
    receiver = user.email
    temp = ''
    for room_number in booking.room_number:
        temp = temp + room_number + ", "
    temp = temp[:len(temp) - 2]
    body = "Hotel " + booking.hotel_name + " has process your booking created on " + booking.created \
           + "with room numbers " + temp
    yag = yagmail.SMTP(user='dung.nguyentien1998@gmail.com', password='Tiendung1098')
    yag.send(
        to=receiver,
        subject="Notification about booking at hotel " + booking.hotel_name,
        contents=body
    )


