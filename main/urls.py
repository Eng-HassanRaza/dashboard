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
    path('insights/catagories/<slug:catagory>/', views.insight_catagory, name='insight_catagory_page'),
    path('insights/question-answer', views.insight_question_answer, name='insight_question_answer'),
    path('about', views.success_stories, name='insight_success_stories'),
    path('contact', views.contact_us, name='contact-us'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('pricing', views.pricing, name='pricing'),
    path('team', views.team, name='team'),
]
