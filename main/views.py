from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Q
from .models import Comment, Product, Category
from .forms import CommentForm


# def home(request):
#     return render(request, 'index.html')
class HomeView(View):

    def get(self, request):
        form = CommentForm()
        products = Product.objects.all()
        comments = Comment.objects.all()
        return render(request, 'index.html', {
            'comments': comments,
            'products': products,
            'form': form
        })

    def post(self, request):
        form = CommentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            message = form.cleaned_data.get('message')

            comment = Comment.objects.create(
                name=name,
                email=email,
                phone=phone,
                message=message
            )
            comment.save()
        return redirect('/')


def about(request):
    return render(request, 'about.html')


def what_we_do(request):
    return render(request, 'what-we.html')


def blog(request):
    return render(request, 'blog.html')


class Contact(LoginRequiredMixin, View):
    def get(self, request):
        form = CommentForm()
        return render(request, 'contact.html', {
            'form': form
        })

    def post(self, request):
        form = CommentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            message = form.cleaned_data.get('message')

            msg = f'''
    {message}
    
    Full name: {name}
    email: {email}
    phone number: {phone} 
                '''

            send_mail(
                'Yangi xabar',
                msg,
                name,
                ['nqobulov571@gmail.com']
            )
        return redirect('contact')


class Categories(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'category.html', )

    def post(self, request):
        name = request.POST.get('name')
        category = Category.objects.create(
            name=name
        )
        category.save()
        return redirect('/')


class Search(View):
    def get(self, request):
        name = request.GET.get('Q', '')
        product1 = Product.objects.filter(title__icontains=name)
        print(product1)
        return render(request, 'search.html')


class Math(View):
    def get(self, request):
        num1 = request.GET.get('num1', 0)
        num2 = request.GET.get('num2', 0)
        add = int(num1) + int(num2)
        add = str(add)
        print(type(num1))
        print(type(add))
        print(add)
        return render(request, 'math.html', {
            'add': add
        })
