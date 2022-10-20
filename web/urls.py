from django.urls import path
from . import views

app_name='web'

urlpatterns = [
    path('base',views.base,name="base"),
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),

    path('news/',views.news,name="news"),
    path('news-single/<str:id>/',views.singleNews,name="news-single"),
    path('explore/',views.explore,name="explore"),

    path('event/',views.event,name="event"),
    path('event-single/',views.eventsingle,name="event-single"),
    path('contact/',views.contact,name="contact"),
    path('departments/',views.departments,name="departments"),
    path('donation/', views.donation, name="donation"),
    path('gallery/', views.gallery, name="gallery"),

    path('volunteer/', views.volunteer, name="volunteer"),
    path('city-jobs-all/',views.career_all, name="city_jobs_all"),
    path('history&tourism/',views.history_tourism, name="history_tourism"),
    path('muncipality&village/',views.muncipality_village, name="muncipality_village"),
    path('education/',views.education, name="education"),
    path('health&hospitals/',views.health_hospital, name="health_hospital"),
    path('business/',views.business, name="business"),
    path('help-line-services/',views.help_line, name="help_line"),


]