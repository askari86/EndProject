from django import forms
from blog.models import Comment
from captcha.fields import CaptchaField

class Commentform(forms.Form):
    captcha = CaptchaField()
    class Meta :
        model = Comment
        filds = ['name', 'email', 'subject', 'message' , 'post']