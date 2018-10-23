"""wallpapermanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from wallpapermanagement import views
from userauthentication import views as uviews
urlpatterns = [
    path('', views.home, name="home"),

    path('login/', views.login, name="login"),
    
    path('contact-us/', views.contact_us, name="contact_us"),
    
    path('register', views.register, name="register"),
    
    path('reset/password', views.reset_password, name="reset_password"),
    
    path('about', views.about, name="about"),

    path('about', views.wallpaper, name="wallpaper"),
    
    path('profile', views.profile, name="profile"),
    
    path('categories', views.categories, name='Categories'),
    
    path('category/<str:cat_name>', views.category, name='category'),
]
