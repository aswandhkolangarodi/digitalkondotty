from django.urls import path
from . import views

app_name='web'

urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),

    path('news/',views.news,name="news"),
    path('news-single/<str:id>/',views.singleNews,name="news-single"),
    path('explore/',views.explore,name="explore"),

    path('event/',views.event,name="event"),
    path('event-single/<str:id>',views.eventsingle,name="event-single"),
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
    path('explore-community-single/<str:id>', views.explore_comunity_single, name = "explore_comunity_single"),
    path('single-job/<str:id>', views.single_job, name = 'single_job'),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('forget-password/', views.forget_password, name="forget-password"),
    path('reset-password/<token>/',views.reset_password, name="reset-password"),
    path('search',views.search_result, name="search")
    


]