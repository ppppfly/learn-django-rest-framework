# -*- coding: utf-8 -*-
from core import views
from django.conf.urls import url

urlpatterns = [
    url(r'^list/$', views.list, name='list'),
]
