from django.shortcuts import render,redirect
from .forms import JobAdd
from jobs.models import Job, JobAppliedUsers, Profile
from django.contrib import messages

# Create your views here.
def index(request):
    
    if 'user' not in request.session:
        return redirect('web:login')
    email = request.session['user']
    user = Profile.objects.filter(email = email).first()
    job_applyed_users = JobAppliedUsers.objects.filter(job__user =user ).order_by('-id')
    jobs = Job.objects.filter(user = user)
    return render(request, "jobs/index.html",{'jobs':jobs,'job_applyed_users':job_applyed_users})

def add_jobs(request):
    if 'user' not in request.session:
        return redirect('web:login')
    form = JobAdd()
    email = request.session['user']
    user = Profile.objects.get(email = email)
    if request.method =="POST":
        form = JobAdd(request.POST,request.FILES)
        if form.is_valid():
            saved_obj = form.save()
            Job.objects.filter(id=saved_obj.id).update(user = user)  
            messages.success(request, "Job added succesfully")
            return redirect('jobs:add-job')
    return render(request, "jobs/add-jobs.html",{'form':form})


def logout(request):
    try:
        del request.session['user']
    except:
        return redirect('web:login')
    return redirect('web:login')