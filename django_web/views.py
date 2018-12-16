from django.shortcuts import render, redirect
from django_web import models
from django.contrib.auth.hashers import make_password, check_password


# Create your views here.


def home(request):
    # 确认session中的用户是否存在
    name = request.session.get('name', None)
    if name:
        return render(request, 'Home.html', {'name': name})
    return render(request, 'Home.html')


def home_quit(request):
    # 移除session中的用户
    if request.session['name']:
        del request.session['name']
        return redirect('/home')
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
                if check_password(password, user.password):
                    request.session['name'] = user.name
                    return redirect('/home')
                else:
                    message = "密码错误"
            except:
                message = "用户名不存在"
            return render(request, "Login.html", {'message': message})
    return render(request, "Login.html")


def register(request):
    if request.method == "POST":
        uid = request.POST.get('id')
        name = r'book' + uid
        pw = request.POST.get('pw')
        telephone = request.POST.get('tpn')
        mail = request.POST.get('mail')
        if uid and pw:
            uid = uid.strip()
            name = name.strip()
            pw = pw.strip()
            mail = mail.strip()
        try:
            models.user_info_one.objects.create(user_id=uid, name=name, password=make_password(pw), email=mail)
            return render(request, 'Login.html', {'message': '注册成功，请登陆。'})
        except:
            return render(request, "Register.html", {'message': '用户已经存在'})
    return render(request, "Register.html")


def xuanhuan(request):
    return render(request, "Xuanhuan.html")


def xianxia(request):
    return render(request, "Xianxia.html")


def kehuan(request):
    return render(request, "Kehuan.html")


def Is_login(func):
    def wrapper(request,*args,**kwargs):
        is_login = request.session.get('name', None)
        if is_login:
            return func(request)
        else:
            return redirect('/login')
    return wrapper


@Is_login
def usr_message(request):
    return render(request, "Memo.html")
