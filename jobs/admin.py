from django.contrib import admin

# Register your models here.
from .models import *


class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ['first_name','email','phone']
    search_fields=('first_name','email','phone')
admin.site.register(Profile,ProfileAdmin)


class JobAdmin(admin.ModelAdmin):
    model = Job
    list_display = ['job_title','location','vacancy','phone','email','job_type','status']
    search_fields=('job_title','location','vacancy','phone','email','job_type','date')
    list_filter = ('job_title','location','job_type','date','status')
admin.site.register(Job,JobAdmin)


class JobAppliedUsersAdmin(admin.ModelAdmin):
    model = JobAppliedUsers
    list_display = ['job','name','email','phone']
    search_fields=('job','name','email','phone')
    list_filter = ('job',)
admin.site.register(JobAppliedUsers,JobAppliedUsersAdmin)