from django.shortcuts import render
from .models import Categories, Wallpapers

def  get_available_category():
    return Categories.objects.filter(active=True)

def home(request):
    walls = Wallpapers.objects.all()
    return render(request, 'user/home.html', {'categories':get_available_category(), 'wallpapers':walls})

def categories(request):
    return render(request, 'user/home.html')

def login(request):
    return render(request, 'user/login.html')

def register(request):
    return render(request, 'user/register.html')

def about(request):
    return render(request, 'user/about.html')

def contact_us(request):
    return render(request, 'user/contact_us.html')

def reset_password(request):
    return render(request, 'user/reset_password.html')

def wallpaper(request):
    return render(request, 'user/wallpaper.html')

def category(request, cat_name):
    wallpapers = Wallpapers.objects.filter(category=cat_name)
    return render(request, 'user/category.html', {'categories':get_available_category(),'category': cat_name, 'wallpapers': wallpapers})