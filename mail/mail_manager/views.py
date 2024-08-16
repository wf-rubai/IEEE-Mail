from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .renderData import Data_Manipulation
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
def mail_table(request):

    if request.method == "POST":
        
        if request.POST.get("log_out"):
            auth.logout(request)
            return redirect('mail:login')

    return render(request,'mail_table.html')

@login_required
def mail_editor(request):

    if request.method == "POST":
        
        if request.POST.get("send-btn"):

            mail_subject = request.POST.get('mail-subject')
            task_title = request.POST.get('task-subject')
            deadline = request.POST.get('deadline')
            description = request.POST.get('task_description_details')
            additional_link = request.POST.get('mail-url')

            if Data_Manipulation.save_email_data(mail_subject,task_title,deadline,description,additional_link):
                messages.success(request,"Email Sent")
            else:
                messages.error(request,"Error Sending Email")

            return redirect('mail:mail_table')

    return render(request,'mail_editor.html')

@login_required
def mail_view(request):
    return render(request,'mail_view.html')

def logout(request):
    auth.logout(request)
