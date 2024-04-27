from django.urls import path, include
from .views import *

urlpatterns =[
path('',product,name='products'),
path('home/',home,name='home'),
path('product/<int:pk>/',product_details,name='product_details'),

]