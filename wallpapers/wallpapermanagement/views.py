from django.shortcuts import render

def home(request):
    return render(request, 'user/home.html', {'items':[1,2,3,4,5,6]})
def categories(request):
    return render(request, '')