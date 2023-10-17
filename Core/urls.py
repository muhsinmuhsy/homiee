from django.urls import path
from Core.views import *

urlpatterns = [
    path('', index, name='index'),
    
    path('get-placeorder/',get_placeorder,name='get-placeorder')
]