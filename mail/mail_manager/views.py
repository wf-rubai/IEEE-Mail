from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from django.contrib import messages

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

def mail_table(request):
    return render(request,'mail_table.html')

def mail_editor(request):
    return render(request,'mail_editor.html')

def mail_view(request):
    return render(request,'mail_view.html')
