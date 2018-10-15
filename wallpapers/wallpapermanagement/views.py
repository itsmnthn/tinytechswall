from django.shortcuts import render
from .models import Categories

def home(request):
    return render(request, 'user/category.html', {'items': [1, 2, 3, 4, 5, 6]})


def categories(request):
    categories = Categories.objects
    return render(request, 'user/category.html', {'categories': categories})
