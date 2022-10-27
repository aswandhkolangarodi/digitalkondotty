
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('web.urls')),
    path('job-portal/',include('jobs.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Digital Kondotty Administration"
admin.site.site_title = "Digital Kondotty Admin Portal"
admin.site.index_title = "Welcome to Digital Kondotty Admin Portal"