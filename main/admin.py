from django.contrib import admin
from .models import Product, Category, Comment, Service

# Register your models here

admin.site.register((Product, Category, Comment, Service))
