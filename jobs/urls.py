from django.urls import path
from . import views

app_name='jobs'

urlpatterns = [
  path('',views.index, name ="home"),
  path('add-job/',views.add_jobs, name ="add-job"),
  path('logout/',views.logout, name ="logout"),

]