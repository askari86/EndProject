from django import forms
from website.models import Contact , newslettr
from captcha.fields import CaptchaField

class ContactForms(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Contact
        fields=  '__all__' 

class ewslettr(forms.ModelForm):

    class Meta():
        model = newslettr
        fields= '__all__'