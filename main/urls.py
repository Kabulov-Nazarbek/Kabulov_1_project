from django.urls import path
from .views import HomeView, About, WhatWeDo, Blog, Contact, Categories, Search, Math

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('maths/', Math.as_view(), name='math'),
    path('what-we-do/', WhatWeDo.as_view(), name='what we do'),
    path('blog/', Blog.as_view(), name='blo'),
    path('contact/', Contact.as_view(), name='contact'),
    path('category/', Categories.as_view(), name='category'),
    path('search/', Search.as_view(), name='search'),

]
