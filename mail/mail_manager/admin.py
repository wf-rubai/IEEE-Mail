from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(NewEmail)
class Email_Admin(admin.ModelAdmin):
    list_display = [
        'id', 'mail_subject' , 'task_title' , 'deadline' , 'description' ,  'additional_link'
    ]