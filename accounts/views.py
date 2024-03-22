from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, logout,login
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from django.contrib.auth.models import User
import re

# Create your views here.

def login_view(request):
    msg = ""
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', username):
            email = username
            user = User.objects.filter(email=email).first()
            if user:
                username = user.username
            user = authenticate(request, username=username, password=password)
        else:
            user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            msg = "Invalid credentials. Please try again."
            messages.error(request, msg)
    form = AuthenticationForm()
    context = {'form': form, 'msg': msg}
    return render(request, 'accounts/login.html', context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

def signup_view(request):
   if not request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomUser(request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request,messages.SUCCESS,'You have successfully registered')
                return redirect('/')
            else:
                messages.add_message(request,messages.ERROR,'Something went wrong ! Try again')
        form = CustomUser()
        context = {'form': form}
        return render(request, 'accounts/signup.html',context)   
class CustomUser(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email', 'username','first_name', 'last_name', 'password1', 'password2')



