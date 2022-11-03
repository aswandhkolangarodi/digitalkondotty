from django.conf import settings 
# html email required stuff

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from jobs.models import *

def forget_password_email(token):
    user = Profile.objects.filter(forget_password_token=token).first()
    html_content = render_to_string("email/forget-password.html",{'user':user})
    text_content = strip_tags(html_content)
    subject = 'Reset Your Password'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user.email]
    email_obj = EmailMultiAlternatives(subject, text_content, email_from, recipient_list)
    email_obj.attach_alternative(html_content, "text/html")
    email_obj.send()



def job_add_email(email):
    job = Job.objects.filter(user__email=email).last()
    html_content = render_to_string("email/job-added.html",{'job':job})
    text_content = strip_tags(html_content)
    subject = 'NEW JOB ADDED'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [settings.EMAIL_HOST_USER]
    email_obj = EmailMultiAlternatives(subject, text_content, email_from, recipient_list)
    email_obj.attach_alternative(html_content, "text/html")
    email_obj.send()