

from django.urls import path
from authapp import views
urlpatterns = [
   path("login/", views.login_page, name="login page"),
   path("signup/", views.signup, name="signup page"),
   path("logout/", views.logout_page, name="logout page")
]