from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'Home.html')


def login(request):
    return render(request, "Login.html")


def register(request):
    return render(request, "Register.html")


def xuanhuan(request):
    return render(request, "Xuanhuan.html")


def xianxia(request):
    return render(request, "Xianxia.html")


def kehuan(request):
    return render(request, "Kehuan.html")
