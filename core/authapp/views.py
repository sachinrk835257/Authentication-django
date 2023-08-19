from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def login_page(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email,password)

        return redirect('/auth/login/')


    return render(request,'auth/login.html')

def signup(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        print(email,pass1,pass2)
        if pass1 != pass2 :
            return redirect('/auth/signup/')
    
        return redirect('/auth/signup/')


    return render(request,'auth/signup.html')

def logout_page(request):
    return HttpResponse("logout")
