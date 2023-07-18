from django.contrib.auth import get_user_model

from celery import shared_task
from django.core.mail import send_mail
from proj import settings

@shared_task(bind=True)
def test_func(self):
    for i in range(10):
        print(i)
    return "Done"


# @shared_task(bind=True)
# def send_mail(self):
#     users = get_user_model().objects.all()
#     for user in users:
#         mail_subject = "hi celery testing"
#         message = "hello"
#         to_email = user.email
#         send_mail = (
#             subject = mail_subject,
#             message = message,
#             from_email = settings.EMAIL_HOST_USER,
#             recipient_mail = [to_email],
#             fail_silently = True
#         )
#     return "Done"