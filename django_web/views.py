from django.shortcuts import render, redirect
from django_web import models
from django.contrib.auth.decorators import login_required


# Create your views here.


def home(request):
    # 确认session中的用户是否存在
    name = request.session.get('name', None)
    if name:
        return render(request, 'Home.html', {'name': name})
    return render(request, 'Home.html')


def home_quit(request, quit_id):
    if quit_id:
        del request.session['name']
        return render(request, 'Home.html',{'message': 'quit success'})
    return render(request, 'Home.html', {'message': 'is not quit!'})


def login(request):
    if request.method == "POST":
        name = request.POST.get("name")
        password = request.POST.get("pw")
        if name and password:
            name = name.strip()
            password = password.strip()
            try:
                user = models.user_info_one.objects.get(user_id=name)
                if password == user.password:
                    request.session['name'] = user.name
                    return redirect('/home')
                else:
                    message = "密码错误"
            except:
                message = "用户名不存在"
            return render(request, "Login.html", {'message': message})
    return render(request, "Login.html")


def register(request):
    return render(request, "Register.html")


def xuanhuan(request):
    return render(request, "Xuanhuan.html")


def xianxia(request):
    return render(request, "Xianxia.html")


def kehuan(request):
    return render(request, "Kehuan.html")


@login_required
def usr_message():
    pass
