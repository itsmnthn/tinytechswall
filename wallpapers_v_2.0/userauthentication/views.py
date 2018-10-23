from django.shortcuts import render

def log(request):
    return render(request, 'user/login.html')