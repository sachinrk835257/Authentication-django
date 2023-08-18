from django.urls import path, include
from app1 import views

urlpatterns = [
    path('', views.index, name="Go to home page"),
    path('auth/', include('authapp.urls'), name="Go to authentication process")
]