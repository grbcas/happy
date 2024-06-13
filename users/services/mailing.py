from django.conf import settings
from celery import shared_task
from django.core.mail import send_mail


@shared_task
def notify(name, email):
    print(f'notify {email} >>> {name} celebrates birthday today')

    subject = f'Notification'
    message = f'Notification: {name} celebrates birthday today'

    send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email, ]
    )
