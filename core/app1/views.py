from django.shortcuts import render

# Create your views here.
def index(request):
    title = '''HOME - PAGE'''
    return render(request, 'index.html')
