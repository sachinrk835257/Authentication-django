

from django.urls import path
from authapp import views
urlpatterns = [
   path("login/", views.login_page, name="login page"),
   path("signup/", views.signup, name="signup page"),
   path("forgot_password/", views.forgot_password, name="forgot password"),
   path("change_password/<token>/", views.change_password, name="change passowrd"),
   path("logout/", views.logout_page, name="logout page")
]