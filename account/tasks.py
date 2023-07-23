from celery import shared_task
import os
from django.core.mail import send_mail
from django.template.loader import render_to_string


@shared_task(expires=3600)
def new_user_email_notification(new_user):
    recipient_email = 'yalisanda@gmail.com'
    context = {
        'username': new_user,
        'cafe_name': 'Girosmani Cafe',
        'order_url': 'https://qimeer.online/cafe/',
    }
    html_content = render_to_string('account/letter_registration_confirmation.html', context)
    from_email = os.getenv('EMAIL_HOST_USER')
    subject = 'Welcome to Girosmani Cafe - Registration Confirmation'
    send_mail(
        subject=subject,
        message='Welcome to Girosmani',
        html_message=html_content,
        from_email=from_email,
        recipient_list=[recipient_email],
        fail_silently=False)

