import re

from django import forms
from django.forms.widgets import SelectMultiple, TextInput, Textarea, EmailInput, CheckboxInput,URLInput, Select, NumberInput, RadioSelect, FileInput,ClearableFileInput, PasswordInput


from .models import *
from django.core.exceptions import ValidationError



def phone_number_validation(value):
    
    if not re.compile(r'[0-9]\d{9}$').match(value):
        raise ValidationError('This is Not Valid Phone Number')
    
class JobAdd(forms.ModelForm):
        phone = forms.CharField(validators=[phone_number_validation],max_length=10,min_length=10,widget=forms.TextInput(attrs={'placeholder':'phone','class':'form-control','name':'phone','id':'phone'}))
        class Meta:
            model = Job
            fields = ['job_title', 'location','vacancy','phone','email','basic_requirements','job_type','about_job','about_company']
            widgets= {
                'job_title': forms.TextInput(attrs={'placeholder':'Job title','class':'form-control','id':'job_title','name':'job_title'}),
                'location': forms.TextInput(attrs={'placeholder':'location','class':'form-control','id':'location','name':'location'}),
                'vacancy': forms.NumberInput(attrs={'placeholder':'vacancy','class':'form-control','name':'vacancy','id':'vacancy'}),
                'phone': forms.TextInput(attrs={'placeholder':'phone','class':'form-control','name':'phone','id':'phone'}),
                'email': forms.EmailInput(attrs={'placeholder':'email','class':'form-control','name':'email','id':'email'}),
                'basic_requirements': forms.Textarea(attrs={'placeholder':'basic requirements','rows':4,'class':'form-control','name':'vacancy','id':'vacancy'}),
                'job_type': forms.Select(attrs={'placeholder':'vacancy','class':'form-control','name':'vacancy','id':'vacancy'}),
                'about_job': forms.Textarea(attrs={'placeholder':'about_job','rows':4,'class':'form-control','name':'about_job','id':'about_job'}),
                'about_company': forms.Textarea(attrs={'placeholder':'about_company','rows':4,'class':'form-control','name':'about_company','id':'about_company'})
            }