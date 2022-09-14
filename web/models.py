from distutils.command.upload import upload
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
    news_author = models.CharField(max_length=100)
    author_image = VersatileImageField(upload_to = "author image")

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

