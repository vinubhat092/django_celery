from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.test),
    path('sendmail/',views.send_mail_to_all),
    
]