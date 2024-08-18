from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from mail_manager.email_handler import EmailHandler

# Create your views here.

def signup(request):
    
    if request.method == "POST":

        if request.POST.get("sign_up"):

            username_ = request.POST.get('user_username')
            email_ = request.POST.get('user_email')
            password_ = request.POST.get('user_password')
            confirm_password_ = request.POST.get('confirm_password')

            if (password_ == confirm_password_):
                if User.objects.filter(username = username_).exists():
                    messages.error(request,"User exists")
                    pass
                else:
                    user = User.objects.create_user(username = username_, email = email_, password = password_)
                    user.save()
                    messages.success(request,"User created successfully")
                    return redirect('mail:login')
            else:
                messages.error(request,"Password do not match")
                return redirect('mail:signup')
            
            
    return render(request,'signup.html')


def login(request):

    if request.method == "POST":

        if request.POST.get("login"):

            username_ = request.POST.get('user_username')
            password_ = request.POST.get('user_password')

            user = auth.authenticate(username = username_, password = password_)

            if user is not None:
                auth.login(request,user)
                return redirect('mail:mail_table')
            else:
                messages.error(request,"Invalid username or password")
                return redirect('mail:login')

    return render(request,'login.html')

@login_required
def logout(request):
    auth.logout(request)
    return redirect('mail:login')

@login_required
def mail_table(request):
    return render(request,'mail_table.html')

@login_required
def mail_editor(request):

    if request.method == 'POST':
        if 'send_email' in request.POST:
            EmailHandler.send_emails(request)
        return redirect('mail:mail_editor')

    return render(request,'mail_editor.html')

@login_required
def mail_view(request):
    return render(request,'mail_view.html')
