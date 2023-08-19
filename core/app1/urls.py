
from django.urls import path, include
from app1 import views
urlpatterns = [
    path('',views.index, name="home page"),
    path("auth/", include('authapp.urls'), name="go to authentication page")
]