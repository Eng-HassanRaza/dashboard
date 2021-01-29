# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index-page'),
    path('insights/', views.insight, name='insight-page'),
    path('insights/<int:id>/', views.insight_post, name='insight_post_page'),
]
