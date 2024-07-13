from django.contrib import admin
from django.urls import path
from mail_manager import views

urlpatterns = [
    path('mails/', views.mail_table, name='mail_table'),
    path('mails/draft/', views.mail_editor, name='mail_editor'),
    path('mails/views/', views.mail_view, name='mail_view'),
    path('login/', views.login, name='login'),
    path('signin/', views.signin, name='signin'),
]