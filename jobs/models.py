from enum import unique
from random import choices
from django.db import models

# Create your models here.


class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=13)
    password = models.CharField(max_length=30)


    def __str__(self):
        return self.first_name


class Job(models.Model):
    CHOICES = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
    ('Internship', 'Internship'),
    ('Remote', 'Remote'),
)   
    user = models.ForeignKey(Profile,on_delete=models.CASCADE,blank=True,null=True,related_name='user')
    job_title = models.CharField(max_length=500)
    location = models.CharField(max_length=100)
    vacancy = models.IntegerField()
    phone = models.CharField(max_length = 10)
    email = models.EmailField()
    basic_requirements = models.TextField()
    job_type = models.CharField(max_length=100,choices=CHOICES)
    about_job = models.TextField()
    about_company = models.TextField()
    date = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    status  =models.BooleanField(default = False)