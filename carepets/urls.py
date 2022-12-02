"""carepets URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from home.views import home
from adoption.views import adoption
from blog.views import blog
from contact.views import contact
from shop.views import shop
from gallery.views import gallery
from about.views import about
from sell_post.views import sellpost
from adoption_post.views import adoptionpost
from login.views import login,register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',login,name='login'),
    path('register/',register,name='register'),
    path('home/',home,name='home'),
    path('adoption/',adoption,name='adoption'),
    path('blog/',blog,name='blog'),
    path('contact/',contact,name='contact'),
    path('shop/',shop,name='shop'),
    path('gallery/',gallery,name='gallery'),
    path('about/',about,name='about'),
    path('post_for_sell/',sellpost,name='sellpost'),
    path('adoptionpost/',adoptionpost,name='adoptionpost'),
]
