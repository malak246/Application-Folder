from django.contrib import admin
from .models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=('name','price','discriptoion')
    list_filter=('name','price','discriptoion')

    fieldsets=((
        'Avalability',{
            'fields':('name','discriptoion')
        }
    ),)
# Register your models here.
