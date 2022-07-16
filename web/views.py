from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request,'web/partials/base.html')

def home(request):
    return render(request,'web/index.html')

def about(request):
    return render(request,'web/about.html')

def news(request):
    return render(request,'web/news.html')

def singleNews(request):
    return render(request,'web/news-single.html')

def explore(request):
    return render(request,'web/explore.html')