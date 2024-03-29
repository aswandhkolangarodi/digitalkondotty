
from django.db import models
from tinymce.models import HTMLField
from versatileimagefield.fields import VersatileImageField
# Create your models here.




# class Profile(models.Model):
#     user = models.OneToOneField( , on_delete=models.CASCADE)
#     status = models.BooleanField()

class News(models.Model):
    news_catagory = models.CharField(max_length=100)
    news_heading = models.CharField(max_length=500)
    news_date = models.DateTimeField()
    news_image = VersatileImageField(upload_to = "news")
    news_content = HTMLField()
    

    def __str__(self):
        return self.news_heading

    class Meta:
        verbose_name_plural = "News"

class History_Tourism(models.Model):
    history_heading = models.CharField( max_length=100)
    history_image = VersatileImageField(upload_to = "Explore city images")
    history_description = HTMLField()

    def __str__(self):
        return self.history_heading

    class Meta:
        verbose_name_plural = "History And Tourism"

class Municipality_Villages(models.Model):
    village_head = models.CharField( max_length=100)
    village_image = VersatileImageField(upload_to = "Explore city images")
    village_phone= models.CharField( max_length=100)
    village_address = HTMLField()

    def __str__(self):
        return self.village_head

    class Meta:
        verbose_name_plural = "Municipality And Villages"


class BusinesAndShops(models.Model):
    shop_name = models.CharField( max_length=100)
    shop_image = VersatileImageField(upload_to = "Explore city images")
    phone = models.CharField(max_length=13, default="+91")
    email = models.EmailField(null=True, blank=True)
    def __str__(self):
        return self.shop_name

    class Meta:
        verbose_name_plural = "Busines And Shops"


class School(models.Model):
    school_name = models.TextField()

    def __str__(self):
        return self.school_name

class College(models.Model):
    college_name = models.TextField()

    def __str__(self):
        return self.college_name

class Helpline_Service(models.Model):
    helpline_head = models.CharField( max_length=100)
    helpline_image = VersatileImageField(upload_to = "Explore city images")
    helpline_phone= models.CharField( max_length=100)
    helpline_address = HTMLField()

    def __str__(self):
        return self.helpline_head

    class Meta:
        verbose_name_plural = "Helpline Services"


class Health_Hospital(models.Model):
    hospital_head = models.CharField( max_length=100)
    hospital_image = VersatileImageField(upload_to = "Explore city images")
    hospital_phone= models.CharField( max_length=100)
    hospital_address = HTMLField()

    def __str__(self):
        return self.hospital_head

    class Meta:
        verbose_name_plural = "Health And Hospital"

class Testimonial(models.Model):
    testimonial = models.TextField()
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=100)
    person_img = models.ImageField(upload_to="testimonial")

    def __str__(self):
        return self.name

class Gallery(models.Model):
    gallery = VersatileImageField(upload_to = "gallery")
    image_description = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Gallery"

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

    class Meta:
        verbose_name_plural = "Explore Comunity"
        