from django.contrib import admin
from web.models import *
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ['user','status']
    search_fields=('user',)
admin.site.register(Profile,ProfileAdmin)

class NewsAdmin(admin.ModelAdmin):
    model = News
    list_display = ['news_heading','news_catagory','news_date','news_content']
    search_fields=('news_heading','news_catagory','news_date','news_content')

admin.site.register(News, NewsAdmin)

class TestimonialAdmin(admin.ModelAdmin):
    model = Testimonial
    list_display = ['name','testimonial']
    search_fields=('name','testimonial')
admin.site.register(Testimonial,TestimonialAdmin)

class EventAdmin(admin.ModelAdmin):
    model = Event
    list_display = ['event_heading','event_catagory','event_date','event_location']
    search_fields=('event_heading','event_catagory','event_date','event_location')
admin.site.register(Event,EventAdmin)

class GalleryAdmin(admin.ModelAdmin):
    model = Gallery
    list_display = ['image_description']
admin.site.register(Gallery,GalleryAdmin)

class ContactAdmin(admin.ModelAdmin):
    model = Contact
    list_display = ['name','email','subject','message']
    search_fields=('name','email','subject','message')
admin.site.register(Contact,ContactAdmin)

class OfficialAdmin(admin.ModelAdmin):
    model = Official
    list_display = ['officials_name','officials_designation','officials_about']
    search_fields=('officials_name','officials_designation','officials_about')
admin.site.register(Official,OfficialAdmin)

class ExploreComunityAdmin(admin.ModelAdmin):
    model = ExploreComunity
    list_display = ['comunity_name','president_name','vice_president_name','secretary_name','chairman_name']
    search_fields=('comunity_name','president_name','vice_president_name','secretary_name','chairman_name')
admin.site.register(ExploreComunity,ExploreComunityAdmin)


class History_TourismAdmin(admin.ModelAdmin):
    model = History_Tourism
    list_display = ['history_heading']
    search_fields=('history_heading','history_description')
admin.site.register(History_Tourism,History_TourismAdmin)

class Municipality_VillagesAdmin(admin.ModelAdmin):
    model = Municipality_Villages
    list_display = ['village_head','village_phone']
    search_fields=('village_head','village_phone')
admin.site.register(Municipality_Villages,Municipality_VillagesAdmin)

class Helpline_ServiceAdmin(admin.ModelAdmin):
    model = Helpline_Service
    list_display = ['helpline_head','helpline_phone']
    search_fields=('helpline_head','helpline_phone')
admin.site.register(Helpline_Service,Helpline_ServiceAdmin)

class Health_HospitalAdmin(admin.ModelAdmin):
    model = Health_Hospital
    list_display = ['hospital_head','hospital_phone']
    search_fields=('hospital_head','hospital_phone')
admin.site.register(Health_Hospital,Health_HospitalAdmin)

class BusinesAndShopsAdmin(admin.ModelAdmin):
    model = BusinesAndShops
    list_display = ['shop_name','phone','email']
    search_fields=('shop_name','phone','email')
admin.site.register(BusinesAndShops,BusinesAndShopsAdmin)

class SchoolAdmin(admin.ModelAdmin):
    model = School
    list_display = ['school_name']
    search_fields=('school_name',)
admin.site.register(School,SchoolAdmin)

class CollegeAdmin(admin.ModelAdmin):
    model = College
    list_display = ['college_name',]
   
admin.site.register(College,CollegeAdmin)
