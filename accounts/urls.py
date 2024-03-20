from accounts.views import *
from django.urls import path
app_name='accounts'

urlpatterns=[
    path('login/' ,login_view , name='login')
]