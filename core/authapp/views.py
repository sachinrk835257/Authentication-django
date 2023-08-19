from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login_page(request):
    return HttpResponse("login")

def signup(request):
    return HttpResponse("signup")

def logout_page(request):
    return HttpResponse("logout")
