from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'send', views.send),
    url(r'by_theme', views.send_by_theme),
    url(r'add_user', views.add_user),
    url(r'^image_load/$', views.image_load, name='image_load'),
]
