from django.shortcuts import render
from web.models import *
# Create your views here.

def base(request):
    return render(request,'web/partials/base.html')

def home(request):
    news = News.objects.all().order_by('-id')[:4]
    context = {
        "news":news
    }
    return render(request,'web/index.html',context)

def about(request):
    return render(request,'web/about.html')


def news(request):
    return render(request,'web/news.html')

def singleNews(request):
    return render(request,'web/news-single.html')

def explore(request):
    return render(request,'web/explore.html')

def event(request):
    return render(request,'web/event.html')

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