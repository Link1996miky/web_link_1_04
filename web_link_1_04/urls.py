"""web_link_1_04 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
import django_web.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', django_web.views.home),
    path('login/', django_web.views.login),
    path('register/', django_web.views.register),
    path('user/', django_web.views.usr_message),
    path('xuanhuan/', django_web.views.xuanhuan),
    path('xianxia/', django_web.views.xianxia),
    path('kehuan/', django_web.views.kehuan),

]
