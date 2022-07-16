from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request,'web/partials/base.html')

def home(request):
    return render(request,'web/index.html')

def about(request):
    return render(request,'web/about.html')

def event(request):
    return render(request,'web/event.html')
