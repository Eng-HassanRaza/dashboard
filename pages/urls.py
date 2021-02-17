# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from . import views

urlpatterns = [
    path('web_hosting', views.web_hosting, name='web_hosting'),
    path('reseller_hosting', views.reseller_hosting, name='reseller_hosting'),
    path('impacx', views.impacx_page, name='impacx_page'),
    path('new-pricing', views.pricing_page, name='pricing_page'),
    path('digitialization', views.Digitialization_page, name='digitialization_page'),
]
