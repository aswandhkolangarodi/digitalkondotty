import email
from django.shortcuts import render
from web.models import *
from django.shortcuts import get_object_or_404, render
# Create your views here.

def base(request):
    return render(request,'web/partials/base.html')

def home(request):
    explore_comunity_1 = ExploreComunity.objects.all()[:4]
    explore_comunity_2 = ExploreComunity.objects.all()[4:8]
    news = News.objects.all().order_by('-id')[:4]
    event = Event.objects.all().order_by('-id')[:4]
    testimonial = Testimonial.objects.all()
    official = Official.objects.all()
    context = {
        "news":news,
        "event":event,
        "testimonial":testimonial,
        "official":official,
        "explore_comunity_1":explore_comunity_1,
        "explore_comunity_2":explore_comunity_2,
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
    
def eventsingle(request):
    return render(request,'web/event-single.html')

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
    return render(request, "web/career-all.html")


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
    educational_institution = Educational_Institution.objects.all()
    context = {
        "educational_institution" : educational_institution
    }
    return render(request, 'web/education.html',context)

def health_hospital(request):
    health_hospital = Health_Hospital.objects.all()
    context = {
        "health_hospital" : health_hospital
    }
    return render(request, "web/health_hospital.html",context)

def business(request):
    return render(request, "web/business.html")

def help_line(request):
    helpline_Service = Helpline_Service.objects.all()
    context = {
        "helpline_Service" : helpline_Service
    }
    return render(request, "web/help-line.html")

def explore_comunity_single(request, id):
    data = ExploreComunity.objects.get(id=id)
    return render(request, "web/explore-comunity-single.html",{"data":data})
    
    
