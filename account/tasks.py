from celery import shared_task
from django.core.mail import send_mail
import os


@shared_task(expires=3600)  # time to execute - 1 hour
def new_user_email_notification(user):
    email = 'farbantis@gmail.com' #user.user.email
    subject = f'registration confirmation'
    message = f"""
        Dear {email},
        you successfully registered with pirosmani
        your status is bronze
    """
    # {user.status} is no available here?.
    from_email = os.getenv('EMAIL_HOST_USER')
    recipient_list = ['yalisanda@gmail.com']
    send_mail(subject, message, from_email, recipient_list, fail_silently=False)
