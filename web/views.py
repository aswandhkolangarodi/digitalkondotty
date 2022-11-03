from django.shortcuts import redirect, render
from web.models import *
from django.shortcuts import get_object_or_404, render
# Create your views here.
from jobs.models import *
from django.contrib import messages
from jobs.forms import RequestJob 

from .helpers import forget_password_email
import uuid

def base(request):
    return render(request,'web/partials/base.html')

def home(request):
    explore_all = ExploreComunity.objects.all().count()
    print(explore_all)
    explore_comunity_1 = ExploreComunity.objects.all()[:explore_all/2]
    explore_comunity_2 = ExploreComunity.objects.all()[explore_all/2:explore_all]
    news = News.objects.all().order_by('-id')[:4]
    event = Event.objects.all().order_by('-id')[:4]
    jobs = Job.objects.filter(status = True).order_by('-id')[:3]
    testimonial = Testimonial.objects.all()
    official = Official.objects.all()
    context = {
        "news":news,
        "event":event,
        "testimonial":testimonial,
        "official":official,
        "explore_comunity_1":explore_comunity_1,
        "explore_comunity_2":explore_comunity_2,
        'jobs':jobs,
       
    }
    return render(request,'web/index.html',context)

def about(request):
    return render(request,'web/about.html')


def news(request):
    news = News.objects.all().order_by('-id')
    context = {
        "news" : news
    }
    return render(request,'web/news.html',context)

def singleNews(request, id):
    single_news= get_object_or_404(News,id=id)
    context = {
        "single_news" : single_news
    }
    return render(request,'web/news-single.html',context)

def explore(request):
    return render(request,'web/explore.html')

def event(request):
    event = Event.objects.all().order_by('-id')
    context = {
        "event" : event
    }
    return render(request,'web/event.html',context)
    
def eventsingle(request , id):
    data = Event.objects.get(id=id)
    return render(request,'web/event-single.html',{'data':data})

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact_obj = Contact(name = name,email = email,subject = subject,message = message)
        contact_obj.save()

    return render(request,'web/contact.html')

def departments(request):
    return render(request,'web/departments.html')

def donation(request):
    return render(request, 'web/donation.html')

def volunteer(request):
    return render(request, 'web/volunteer.html')

def gallery(request):
    gallery = Gallery.objects.all()
    context = {
        "gallery":gallery
    }
    return render(request, 'web/gallery.html',context)

def career_all(request):
    jobs = Job.objects.filter(status = True).order_by('-id')
    return render(request, "web/career-all.html",{'jobs':jobs})


def history_tourism(request):
    history_tourism = History_Tourism.objects.all()
    context = {
        "history_tourism":history_tourism
    }
    return render(request, "web/history-tourism.html",context)



def muncipality_village(request):
    municipality_villages = Municipality_Villages.objects.all()
    context = {
        "municipality_villages":municipality_villages
    }
    return render(request, "web/muncipality-village.html",context)

def education(request):
    schools = School.objects.all()
    colleges = College.objects.all()
    context = {
        "schools" : schools,
        'colleges':colleges
    }
    return render(request, 'web/education.html',context)

def health_hospital(request):
    health_hospital = Health_Hospital.objects.all()
    context = {
        "health_hospital" : health_hospital
    }
    return render(request, "web/health_hospital.html",context)

def business(request):
    data = BusinesAndShops.objects.all().order_by('-id')
    return render(request, "web/business.html",{'data':data})

def help_line(request):
    helpline_Service = Helpline_Service.objects.all()
    context = {
        "helpline_Service" : helpline_Service
    }
    return render(request, "web/help-line.html" ,context)

def explore_comunity_single(request, id):
    data = ExploreComunity.objects.get(id=id)
    return render(request, "web/explore-comunity-single.html",{"data":data})


def signup(request):
    try:
        if request.method == "POST":
            first_name = request.POST['first_name']
            email = request.POST['email']
            phone = request.POST['phone']
            password = request.POST['password']
            profile_exist = Profile.objects.filter(email = email).exists()
            if profile_exist:
                messages.warning(request, "User already exist")
                return redirect('web:signup')
            Profile.objects.create(first_name=first_name, email= email, phone=phone, password=password)
            messages.success(request, "Successfully Registered")
            return redirect('web:login')
    except Exception as e:
            print(e)
            messages.warning(request, "Something Went Wrong")
    return render(request, "web/signup.html")
    
def login(request):
    try:
        if request.method == "POST":
            email = request.POST['email']
            password = request.POST['password']
            user = Profile.objects.filter(email = email).first()
            if user is None:
                messages.warning(request, "User not found")
                return redirect('web:login')
            if user.password != password:
                messages.error(request, "Wrong Password")
                return redirect('web:login')
            request.session['user']=email
            return redirect('/job-portal/')
    except Exception as e:
        print(e)
        messages.warning(request, "Something Went Wrong")
    return render(request, "web/login.html")

def single_job(request,id):
    form = RequestJob()
    job=Job.objects.get(id= id)
    if request.method == "POST":
        form = RequestJob(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save()
            JobAppliedUsers.objects.filter(id=instance.id).update(job = job)
            messages.success(request, "Applyed Successfully")
            return redirect(f'/single-job/{id}')
    return render(request,'web/single-job.html',{'job':job,'form':form})


def forget_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        if Profile.objects.filter(email = email).exists() is False:
            messages.error(request, 'User not found')
            return redirect('web:forget-password')
        token = uuid.uuid4()
        user = Profile.objects.filter(email=email).update(forget_password_token=token)
        forget_password_email(token)
        messages.success(request, "An Email is send")
        return redirect('web:forget-password')
    return render(request, 'web/forget-password.html')

def reset_password(request,token):
    if Profile.objects.filter(forget_password_token= token).exists() is False:
        return redirect('web:signup')
    if request.method == 'POST':
        new_password = request.POST['password']
        Profile.objects.filter(forget_password_token= token).update(password=new_password, forget_password_token=uuid.uuid4())
        messages.success(request, 'Password Reset Successfully')
        return redirect('web:login')
    return render(request, "web/reset-password.html")