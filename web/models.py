from distutils.command.upload import upload
from email import message
from django.db import models
from tinymce.models import HTMLField
from versatileimagefield.fields import VersatileImageField
# Create your models here.


class News(models.Model):
    news_catagory = models.CharField(max_length=100)
    news_heading = models.CharField(max_length=500)
    news_date = models.DateTimeField()
    news_image = VersatileImageField(upload_to = "news")
    news_content = HTMLField()
    

    def __str__(self):
        return self.news_heading


class Testimonial(models.Model):
    testimonial = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=100)
    person_img = models.ImageField(upload_to="testimonial")

    def __str__(self):
        return self.name

class Gallery(models.Model):
    gallery = VersatileImageField(upload_to = "gallery")
    image_description = models.CharField(max_length=100)

class Event(models.Model):
    event_catagory = models.CharField(max_length=100)
    event_heading = models.CharField(max_length=100)
    event_description = HTMLField()
    event_date = models.DateField()
    event_start_time = models.TimeField()
    event_end_time = models.TimeField()
    event_location = models.CharField(max_length=1000)
    event_image = VersatileImageField(upload_to = "event")

    def __str__(self):
        return self.event_heading

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Official(models.Model):
    officials_name = models.CharField(max_length=100)
    official_image = VersatileImageField(upload_to="official")
    officials_designation = models.CharField(max_length=100)
    officials_about = models.CharField(max_length=500)

    def __str__(self):
        return self.officials_name

class ExploreComunity(models.Model):
    comunity_name =models.CharField(max_length=100)
    icon_image = VersatileImageField(upload_to = "explorecity")
    content = HTMLField()
    president_name =models.CharField(max_length=100)
    president_image = VersatileImageField(upload_to = "explorecity")
    vice_president_name =models.CharField(max_length=100)
    vice_president_image = VersatileImageField(upload_to = "explorecity")
    secretary_name = models.CharField(max_length=100)
    secretary_image = VersatileImageField(upload_to = "explorecity")
    chairman_name = models.CharField(max_length=100)
    chairman_image = VersatileImageField(upload_to = "explorecity")
    contact_number = models.CharField(max_length=100 ,default="+91")
    whatsapp_number = models.CharField(max_length=100 ,default="+91")

    def __str__(self):
        return self.comunity_name