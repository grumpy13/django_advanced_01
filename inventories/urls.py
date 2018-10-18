from django.contrib import admin
from django.urls import path, include
from .views import inventory_list
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('list/', inventory_list, name='list'),
    
]

