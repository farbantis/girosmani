from celery import shared_task
from django.core.mail import send_mail
import os


# @shared_task(expires=3600)  # time to execute - 1 hour
# def new_user_email_notification(user):
#     email = 'farbantis@gmail.com' #user.user.email
#     subject = f'registration confirmation'
#     message = f"""
#         Dear {email},
#         you successfully registered with pirosmani
#         your status is bronze
#     """
#     # {user.status} is no available here?.
#     from_email = os.getenv('EMAIL_HOST_USER')
#     recipient_list = ['yalisanda@gmail.com']
#     send_mail(subject, message, from_email, recipient_list, fail_silently=False)

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


@shared_task(expires=3600)
def new_user_email_notification(user):
    recipient_email = 'yalisanda@gmail.com'
    context = {
        'username': user,
        'cafe_name': 'Girosmani Cafe',
        'order_url': 'https://qimeer.online/account/registration_confirmation_email/',
    }
    html_content = render_to_string('account/letter_registration_confirmation.html', context)
    from_email = os.getenv('EMAIL_HOST_USER')
    subject = 'Welcome to Girosmani Cafe - Registration Confirmation'
    email = EmailMultiAlternatives(subject, from_email, [recipient_email])
    email.attach_alternative(html_content, "text/html")
    email.send()

    message = 'ordinary email' + html_content + subject
    send_mail(
        subject=subject,
        html_message=html_content,
        from_email=from_email,
        recipient_list=[recipient_email],
        fail_silently=False)

