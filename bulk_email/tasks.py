from celery import shared_task
from celery import Celery
import os
from django.core.mail import send_mail

celery = Celery('tasks', broker='amqp://guest@localhost//') #!

os.environ[ 'DJANGO_SETTINGS_MODULE' ] = "proj.settings"

@shared_task
def send_bulk_emails(subject, message, email_list):
    for email in email_list:
        send_mail(subject, message, 'your_email@example.com', [email])