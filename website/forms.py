from django import forms
from website.models import Contact , newslettr
from captcha.fields import CaptchaField

class ContactForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Contact
        fields=  '__all__' 

class newslettr(forms.ModelForm):

    class Meta():
        model = newslettr
        fields= '__all__'