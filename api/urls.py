# Created by Md.Abdullah Al Mamun
# Project: notes
# File: urls.py
# Email: dev.mamun@gmail.com
# Date: 8/31/2021
# Time: 11:16 PM
# Year: 2021

from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('notes/', views.getNotes),
    path('notes/create/', views.create),
    path('notes/<str:pk>/update/', views.update),
    path('notes/<str:pk>/delete/', views.delete),
    path('notes/<str:pk>/', views.getNote),
]
