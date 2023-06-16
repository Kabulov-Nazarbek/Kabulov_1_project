from django.urls import path
from .views import HomeView, about, what_we_do, blog, Contact, Categories, Search, Math

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', about),
    path('what-we-do/', what_we_do),
    path('blog/', blog),
    path('contact/', Contact.as_view(), name='contact'),
    path('category/', Categories.as_view(), name='category'),
    path('search/', Search.as_view(), name='search'),
    path('math/', Math.as_view(), name='math')
]
