from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.contrib import messages
from authapp.send_mail import send_mail_forgot_password_link
from authapp.models import Profile
import uuid

# Create your views here.


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('password')
        try:
                
            user = authenticate(username = username, password = password)

            if user is not None:
                login(request,user)
                return redirect('/')
            else:
                messages.add_message(request, messages.WARNING,
                                    "INVALID CREDENTIALS!!")
                return redirect('/auth/login/')
        except Exception as e:
            messages.add_message(request, messages.WARNING,
                                 "{}".format(e))
            return redirect('/auth/login/') 

    return render(request, 'auth/login.html')


def signup(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = email
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if pass1 != pass2:
            messages.add_message(request, messages.WARNING,
                                 "PASSWORD NOT MATCH !!")
            return redirect('/auth/signup/')
        try:

            if User.objects.filter(username=username).exists():
                messages.add_message(
                    request, messages.WARNING, "USERNAME IS ALREADY EXIXTS!")
                return redirect('/auth/signup/')
            else:
                user = User.objects.create_user(
                    first_name=first_name, last_name=last_name, email=email, username=email)
                user.set_password(pass1)
                user.save()
                messages.add_message(
                    request, messages.SUCCESS, "USER CREATED SUCCESSFULLY")
                return redirect('/auth/signup/')
        except Exception as e:
            messages.add_message(request, messages.WARNING,
                                 "{}".format(e))
            return redirect('/auth/signup/')

    return render(request, 'auth/signup.html')


def logout_page(request):
    logout(request)
    return redirect('/auth/login/')


def change_password(request):
        title = '''change password'''
        if request.method == 'POST':
            username = request.POST.get('username')
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_password')
            if new_password != confirm_password:
                messages.add_message(request, messages.WARNING,
                                 "PASSWORD MISMATCH!!")
                return redirect('/auth/change_password/')
            try:
                user = User.objects.get(username = username) # change password then should get the user intead of filter
                user.set_password(confirm_password)
                user.save()
                return redirect('/auth/login/')
            except Exception as e:
                messages.add_message(request, messages.WARNING,
                                 "USER NOT FOUND!!")
                return redirect('/auth/change_password/')

            
        return render(request, 'auth/change_password.html',{"title":title,"user_detail":user_detail})

def forgot_password(request):
    title = '''forgot password'''
    if request.method == 'POST':
        email = request.POST.get('email')
        user_obj = User.objects.filter(email = email).first()   #acces only first element which found
        if user_obj is None:
            messages.add_message(request, messages.WARNING,
                                 "USER NOT FOUND!!")
            return redirect('/auth/login/')
        
        token = str(uuid.uuid4())
        # print(user.email)
        profile_obj = Profile.objects.get(user=user_obj.username)
        profile_obj.forget_password_token = token
        profile_obj.save()       
        print("done")

        
        



        

        # send email verification
    return render(request, 'auth/forgot_password.html',{"title":title})