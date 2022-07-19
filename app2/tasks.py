
from celery import shared_task
from django.core.mail import EmailMessage
from django.conf import settings
from celery.decorators import task
# from celery import task
from celery.utils.log import get_task_logger

from app2.email import send_review_email

logger = get_task_logger(__name__)


@task(name="send_review_email_task")
def send_review_email_task(name, email, review):
    print(name)
    print(email)
    print(review)
    logger.info("Sent review email")
    return send_review_email(name, email, review)


@shared_task
def send_congrats_mail(name, mail):
    logger.info("Sent congrats email")
    mail_subject = f"Hi {name}, are you back on the market? We'd love to help."
    mail_body = f"""
Hi {name},

It’s David from coderjob. I noticed your profile on freemob and wanted to touch base to see if you’re looking for a new challenge?

As a reminder, coderjob matches specialists and many other positions within the SDLC to fantastic companies, this is based on both your skills and preferences to ensure you get the right offer, at the right company. Even better, no recruiters, just direct contact with top companies.

Since the last time you used coderjob we've made big changes, we've listened to user feedback and made both product and process improvements which ensure your job search will be quick, frictionless, and transparent.
    """
    email = EmailMessage(mail_subject, mail_body,
                         settings.DEFAULT_FROM_EMAIL, [mail])
    return email.send(fail_silently=False)
