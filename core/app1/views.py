from django.shortcuts import render

# Create your views here.

def index(request):
    title = '''HOME - APP1'''
    return render(request,'index.html',{"title":title})
