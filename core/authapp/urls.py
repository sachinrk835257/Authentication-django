
from django.urls import path, include
from authapp import views

urlpatterns = [
   path('login/',views.login_page, name="login page"),
   path('sign_up/',views.sign_up, name="sign_up page"),
   path('logout/',views.logout_page, name="logout page"),

]