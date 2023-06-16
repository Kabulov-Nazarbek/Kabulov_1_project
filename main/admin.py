from django.contrib import admin
from .models import Product, Category, Comment

# Register your models here

admin.site.register((Product, Category, Comment))
