from django.urls import path
from . import views

app_name='web'

urlpatterns = [
    path('base',views.base,name="base"),
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),

    path('news/',views.news,name="news"),
    path('news-single/',views.singleNews,name="news-single"),
    path('explore/',views.explore,name="explore"),

    path('event/',views.event,name="event"),
    path('contact/',views.contact,name="contact"),
    path('departments/',views.departments,name="departments")


]