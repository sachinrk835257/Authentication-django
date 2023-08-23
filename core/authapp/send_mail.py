from django.core.mail import send_mail
# from django.conf import settings
import os
# from pathlib import Path
# from decouple import config
from dotenv import load_dotenv
load_dotenv()



def send_mail_forgot_password_link(email, token):
    subject = '''this is checking purpose'''
    message = f'''change your password from here http://127.0.0.1:8000/auth/change_password/{token}'''
    recipeint_list = [f"{email}"]
    print(recipeint_list)
    from_email = os.getenv('EMAIL_HOST_USER')
    print(from_email)

    send_mail(subject, message, from_email, recipeint_list)
    return True


