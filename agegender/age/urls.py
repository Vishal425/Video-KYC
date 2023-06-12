from operator import index
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('test',views.test),
    # path('test/otp',views.otp),

]
