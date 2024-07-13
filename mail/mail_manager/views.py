from django.shortcuts import render

# Create your views here.

def mail_table(request):
    return render(request,'mail_table.html')

def mail_editor(request):
    return render(request,'mail_editor.html')

def mail_view(request):
    return render(request,'mail_view.html')

def login(request):
    return render(request,'login.html')

def signin(request):
    return render(request,'signin.html')