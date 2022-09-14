from django.shortcuts import render
from web.models import *
from django.shortcuts import get_object_or_404, render
# Create your views here.

def base(request):
    return render(request,'web/partials/base.html')

def home(request):
    news = News.objects.all().order_by('-id')[:4]
    event = Event.objects.all().order_by('-id')[:4]
    context = {
        "news":news,
        "event":event
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
    return render(request,'web/contact.html')

def departments(request):
    return render(request,'web/departments.html')

def donation(request):
    return render(request, 'web/donation.html')

def gallery(request):
    gallery = Gallery.objects.all()
    context = {
        "gallery":gallery
    }
    return render(request, 'web/gallery.html',context)