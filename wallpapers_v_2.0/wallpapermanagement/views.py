from django.shortcuts import render, Http404, HttpResponse, HttpResponseRedirect
from .models import Categories, Wallpapers
from userauthentication.models import Users


def get_available_category():
    return Categories.objects.filter(active=True)


def home(request):
    walls = Wallpapers.objects.all()
    return render(request, 'user/home.html', {'categories': get_available_category(), 'wallpapers': walls})


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


def wallpaper(request):
    return render(request, 'user/wallpaper.html')


def profile(request):
    walls = Wallpapers.objects.all()
    return render(request, 'user/profile.html', {'categories': get_available_category(), 'wallpapers': walls})


def category(request, cat_name):
    wallpapers = Wallpapers.objects.filter(category=cat_name)
    return render(request, 'user/category.html', {'categories': get_available_category(), 'category': cat_name, 'wallpapers': wallpapers})


def test(request):
    return render(request, 'user/test.html')


# Login section
def login(request):
    return render(request, 'user/login.html')


def do_login(request):
    if request.method != 'POST':
        raise Http404('Only POSTs are allowed')
    try:
        m = Users.objects.get(username=request.POST['username'])
        if m.password == request.POST['password']:
            request.session['member_id'] = m.id
            return render(request, 'user/test.html', data={'usernm': request.POST['username'],
                'password': request.POST['password']})
            # return HttpResponseRedirect('/you-are-logged-in/')
    except:
        return HttpResponse("Your username and password didn't match.")
        # a = Users.objects.get(username=request.POST['username'])
    return render(request, 'user/login.html')

# end login section
