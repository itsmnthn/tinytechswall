from django.shortcuts import render, Http404, HttpResponse, HttpResponseRedirect
from .models import Categories, Wallpapers
from django.contrib.auth.models import User


def home(request):
    walls = Wallpapers.objects.all()
    return render(request, 'user/home.html', {'wallpapers': walls})


def categories(request):
    return render(request, 'user/home.html')


def register(request):
    return render(request, 'user/register.html')


def about(request):
    return render(request, 'user/about.html')


def contact_us(request):
    return render(request, 'user/contact_us.html')


def reset_password(request):
    return render(request, 'user/reset_password.html')


def wallpaper(request, category, slug):
    wallpaper = Wallpapers.objects.get(category=Categories.objects.get(title=category),slug=slug)
    return render(request, 'user/wallpaper.html', {'wallpaper':wallpaper})


def profile(request):
    walls = Wallpapers.objects.all()
    return render(request, 'user/profile.html', {'wallpapers': walls})


def category(request, cat_name):
    wallpapers = Wallpapers.objects.filter(category=Categories.objects.get(title=cat_name))
    return render(request, 'user/category.html', {'category': cat_name, 'wallpapers': wallpapers})

def tag(request, tag):
    wallpapers = Wallpapers.objects.filter(tags__icontains=tag)
    return render(request, 'user/category.html', {'category': tag, 'wallpapers': wallpapers})

def search(request):
    term = request.GET.get('search_nav')
    wallpapers = Wallpapers.objects.filter(
        title__icontains=term,
        tags__icontains=term,
        description__icontains=term,
    )
    return render(request, 'user/category.html', {'category': term, 'wallpapers': wallpapers})


def test(request):
    return render(request, 'user/test.html')
