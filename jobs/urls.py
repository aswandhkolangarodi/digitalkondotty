from django.urls import path
from . import views

app_name='jobs'

urlpatterns = [
  path('',views.index, name ="home"),
  path('jobs-list/',views.jobs, name ="jobs"),
  path('add-job/',views.add_jobs, name ="add-job"),
  path('logout/',views.logout, name ="logout"),
  path('job-approve/<str:token>/',views.job_approve, name ="job-approve"),
  path('job-applied-user-single/<str:id>/',views.job_applied_user_details, name ="job-applied-user-single"),

]