from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'Home.html')


def login(request):
    if request.method == "POST":
        name = request.POST.get("name")
        password = request.POST.get("pw")
        if name and password:
            name = name.strip()
            password = password.strip()
            try:
                user = models.user_info_one.objects.get(name=name)
                if password == user.password:
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
