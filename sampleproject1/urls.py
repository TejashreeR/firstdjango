"""sampleproject1 URL Configuration

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
from django.urls import path
from home1.views import form_view,html_form,booksearch,deletebook,editbook
from home2.views import register


urlpatterns = [
    path('admin/', admin.site.urls),
    path('forms/', form_view,name='form'),
    path('home/', form_view,name='home'),
    path('contact/', form_view,name='contact'),
    path('html/', html_form),
    path('', booksearch),
    path('deletebook/<id>',deletebook),
    path('editbook/<id>',editbook),
    path('register/',register,name='register'),
    #path('',include('blog.urls')),



]
