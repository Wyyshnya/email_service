from celery.decorators import task
from celery.utils.log import get_task_logger
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import random
from django.conf import settings

logger = get_task_logger(__name__)


@task(name='send_email_task')
def send_email_task(template_name, user_list):
    for user in user_list:
        html_message = render_to_string(template_name, {"email": user['email'], "code": random.randint(100000, 999999),
                                                        "first_name": user['first_name'], "second_name": user['second_name']})
        message = strip_tags(html_message)
        send_mail('Email', message, recipient_list=[user['email'], ], from_email=settings.EMAIL_HOST_USER, html_message=html_message)


@task(name='error_handler')
def error_handler(request, exc, traceback):
    print('Task {0} raised exception: {1!r}\n{2!r}'.format(
          request.id, exc, traceback))
