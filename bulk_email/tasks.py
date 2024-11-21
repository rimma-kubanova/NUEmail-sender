from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_bulk_emails(email_subject, email_message, recipient_list):
    for recipient in recipient_list:
        send_mail(
            email_subject,
            email_message,
            "rimma.kubanova@gmail.com",  # Sender email
            [recipient],  # Recipient
            fail_silently=False,
        )
