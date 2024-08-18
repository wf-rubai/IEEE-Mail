from django.contrib import admin
from django.urls import path
from mail_manager import views

app_name = "mail"

urlpatterns = [
    path('mails/', views.mail_table, name='mail_table'),
    path('mails/draft/', views.mail_editor, name='mail_editor'),
    path('mails/views/', views.mail_view, name='mail_view'),
    path('', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
]