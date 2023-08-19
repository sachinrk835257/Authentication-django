from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="/auth/login/")
def index(request):
    title = '''HOME - PAGE'''
    return render(request, 'index.html')
