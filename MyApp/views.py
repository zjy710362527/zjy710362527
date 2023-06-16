from django.http import HttpResponse

from .models import Test
from django.shortcuts import render
from django.contrib import messages
from MyApp import models


def index(request):
    return render(request, "index.html")


def register(request):
    pass


def login(request):
    pass


def logout(request):
    pass


import hashlib


def setPassword(password):
    """
    加密密码，算法单次md5
    :param apssword: 传入的密码
    :return: 加密后的密码
    """
    md5 = hashlib.md5()
    md5.update(password.encode())
    password = md5.hexdigest()
    return str(password)


from django.shortcuts import render
from MyApp.models import UserInfor
from django.shortcuts import HttpResponseRedirect


def register(request):
    if request.method == "POST" and request.POST:
        data = request.POST
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")
        UserInfor.objects.create(
            username=username,
            email=email,
            password=setPassword(password),
        )
        return HttpResponseRedirect('/MyApp/login/')
    return render(request, "register.html")


def login(request):
    if request.method == 'POST' and request.POST:
        email = request.POST.get("email")
        password = request.POST.get("password")
        e = UserInfor.objects.filter(email=email).first()
        if e:
            now_password = setPassword(password)
            db_password = e.password
            if now_password == db_password:
                response = HttpResponseRedirect('/MyApp/index/')
                response.set_cookie("email", e.email)
                return response
        messages.error(request, "登录失败，请确认密码")
    return render(request, "login.html")


def logout(request):
    response = HttpResponseRedirect('/MyApp/login/')
    response.delete_cookie("username")
    return response


def userValid(fun):
    def inner(request, *args, **kwargs):
        username = request.COOKIES.get("email")
        if username:
            return fun(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/MyApp/login/')

    return inner


@userValid
def index(request):
    return render(request, "index.html")


from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Task


def dashboard(request):
    user_count = User.objects.count()
    task_count = Task.objects.count()

    context = {'user_count': user_count, 'task_count': task_count}
    return render(request, 'dashboard.html', context)
