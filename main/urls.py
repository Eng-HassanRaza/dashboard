# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index-page'),
    path('insights/', views.insight, name='insight-page'),
    path('insights/slider/', views.slider, name='insight-page-slider'),
    path('insights/<int:id>/', views.insight_post, name='insight_post_page'),
    path('insights/catagories/<slug:catagory>/', views.insight_catagory, name='insight_catagory_page'),
    path('insights/question-answer', views.insight_question_answer, name='insight_question_answer'),
]
