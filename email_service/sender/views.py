# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from json import loads
from .models import Customer, Theme, ThemeCustomer
from .serializers import CustomerSerializer
from .tasks import send_email_task, error_handler


def add_user(request):
    if request.method == "POST":
        try:
            body = loads(request.body)
            Customer.objects.create_user(body['email'], body['first_name'], body['second_name'])
            return HttpResponse(status=200)
        except Exception as err:
            return HttpResponse(content=err, status=400)
    else:
        return HttpResponse(status=405)


@csrf_exempt
def send(request):
    if request.method == "POST":
        try:
            body = loads(request.body)
            users = []
            for email in body['emails']:
                users.append(CustomerSerializer(Customer.objects.get_by_natural_key(email)).data)
            send_email_task.apply_async((body['template_name'], users), countdown=int(body['countdown']),
                                        link_error=error_handler.s())
            return HttpResponse(status=200)
        except Exception as err:
            return HttpResponse(content=err, status=400)
    else:
        return HttpResponse(status=405)


@csrf_exempt
def send_by_theme(request):
    if request.method == "POST":
        try:
            body = loads(request.body)
            theme = Theme.objects.get_by_natural_key(body['theme'])
            theme_customers = ThemeCustomer.objects.filter(name=theme)
            users = []
            for theme_customer in theme_customers:
                users.append(CustomerSerializer(Customer.objects.get(pk=theme_customer.customer_id_id)).data)
            send_email_task.apply_async((body['template_name'], users), countdown=int(body['countdown']),
                                        link_error=error_handler.s())
            return HttpResponse(status=200)
        except Exception as err:
            return HttpResponse(content=err, status=400)
    else:
        return HttpResponse(status=405)
