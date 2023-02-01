# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import os


def mailing(request):
    html_message = render_to_string('mail_var1.html', {"email": 'jefersonhrm1@gmail.com', "code": 894513})
    message = strip_tags(html_message)
    send_mail('Код для входа', message, recipient_list=['jefersonhrm1@gmail.com', ], from_email='eco.crowd@mail.ru', html_message=html_message)
# Create your views here.
