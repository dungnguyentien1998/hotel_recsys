# import os
# import logging
# from django.conf import settings
# from emails import Message
# from emails.template import JinjaTemplate
# from app.utils.security import TokenType, generate_token
#
#
# # Send email function, with parameters subject, html, environment and received email
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
#         smtp_options['user'] = settings.SMTP_USER
#     if settings.SMTP_PASSWORD:
#         smtp_options['password'] = settings.SMTP_PASSWORD
#
#     # Receive response after send email
#     response = message.send(to=mail_to, render=environment, smtp=smtp_options)
#     logging.info(f'Send email result: {response}')
#
#
# # Send email for new account
# def send_new_account_email(user):
#     # Set up parameters
#     project_name = settings.PROJECT_NAME
#     link = settings.SERVER_HOST
#     subject = f'{project_name} - New account for user {user.email}'
#     token = generate_token(obj=user.uuid, _type=TokenType.NEW_ACCOUNT)
#     with open(os.path.join(os.getcwd(), 'app', 'utils', 'templates', 'new_account.html')) as file:
#         html = file.read()
#
#     send_mail(mail_to=user.email, subject=subject, html=html,
#               environment={'project_name': project_name,
#                            'email': user.email,
#                            'token': token,
#                            'link': link,
#                            })
#
#
# # Send email for new account
# def send_forgot_password(user):
#     # Set up parameters
#     project_name = settings.PROJECT_NAME
#     link = settings.SERVER_HOST
#     subject = f'{project_name} - Forgot password for user {user.email}'
#     token = generate_token(obj=user.uuid, _type=TokenType.FORGOT_PASSWORD)
#     with open(os.path.join(os.getcwd(), 'app', 'utils', 'templates', 'forgot_password.html')) as file:
#         html = file.read()
#
#     send_mail(mail_to=user.email, subject=subject, html=html,
#               environment={'project_name': project_name,
#                            'email': user.email,
#                            'token': token,
#                            'link': link,
#                            })
