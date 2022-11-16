from django.shortcuts import render,redirect
from .forms import JobAdd
from jobs.models import Job, JobAppliedUsers, Profile
from django.contrib import messages

from web.helpers import job_add_email
# Create your views here.
def index(request):
    
    if 'user' not in request.session:
        return redirect('web:login')
    email = request.session['user']
    user = Profile.objects.filter(email = email).first()
    job_applyed_users = JobAppliedUsers.objects.filter(job__user =user ).order_by('-id')
    return render(request, "jobs/index.html",{'job_applyed_users':job_applyed_users,'user':user})


def jobs(request):
    if 'user' not in request.session:
        return redirect('web:login')
    email = request.session['user']
    jobs = Job.objects.filter(user__email = email)
    user = Profile.objects.filter(email = email).first()
    return render(request,'jobs/jobs.html',{'jobs':jobs,'user':user})

def add_jobs(request):
    if 'user' not in request.session:
        return redirect('web:login')
    form = JobAdd()
    email = request.session['user']
    user = Profile.objects.get(email = email)
    if request.method =="POST":
        form = JobAdd(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            saved_obj = form.save()
            Job.objects.filter(id=saved_obj.id).update(user = user)
            job_add_email(email)
            messages.success(request, "Job added succesfully")
            return redirect('jobs:add-job')
    return render(request, "jobs/add-jobs.html",{'form':form,'user':user})


def logout(request):
    try:
        del request.session['user']
    except:
        return redirect('web:login')
    return redirect('web:login')


def job_approve(request, token):
    Job.objects.filter(test_id=token).update(status=True)
    return redirect('web:home')


def job_applied_user_details(request, id):
    if 'user' not in request.session:
        return redirect('web:login')
    email = request.session['user']
    user = Profile.objects.filter(email = email).first()
    job_applied_user = JobAppliedUsers.objects.get(id=id)
    return render(request, 'jobs/job-user-single.html',{'user':user,'job_applied_user':job_applied_user})