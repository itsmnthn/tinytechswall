from django.shortcuts import render
from .models import Categories, Wallpapers

def  get_available_category():
    return Categories.objects.filter(active=True)

def home(request):
    walls = Wallpapers.objects.all()
    return render(request, 'user/home.html', {'categories':get_available_category(), 'wallpapers':walls})

def categories(request):
    return render(request, 'user/home.html')

def category(request, cat_name):
    wallpapers = Wallpapers.objects.filter(category=cat_name)
    return render(request, 'user/category.html', {'categories':get_available_category(),'category': cat_name, 'wallpapers': wallpapers})