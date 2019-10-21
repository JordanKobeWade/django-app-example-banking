"""bank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import path, include
from django.views.generic.base import RedirectView
from accounts.views import (register, dashboard, setup, 
    index, products, please_login, savings_page, checking_page,
    moneymarket_page, cd_page, iracd_page, document_uploader)


urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('cd/', cd_page, name='cd'),
    path('iracd/', iracd_page, name='iracd'),
    path('checking/', checking_page, name='checking'),
    path('dashboard/', dashboard, name='dashboard'),
    path('error/', please_login, name='error'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), 
        name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), 
        name='login'),
    path('moneymarket/', moneymarket_page, name='moneymarket'),
    path('products/', products, name='products'),
    # path('profile/', profile, name='profile'),
    path('profile/setup/', setup, name='setup'),
    path('register/', register, name='register'),
    path('savings/', savings_page, name='savings'),
    path('upload/', document_uploader, name='upload'),
    path('favicon.ico',
        RedirectView.as_view(url=staticfiles_storage.url('favicon.ico')))
]
