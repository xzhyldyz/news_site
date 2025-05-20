from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login as user_login, logout as user_logout, get_user_model
from django.contrib.auth.decorators import login_required
from apps.news.models import Category
User = get_user_model()



def login_view(request):
    categories_menu = Category.objects.all()
    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')
        usr = authenticate(request, username=login, password=password)
        if usr is not None:
            user_login(request, usr)
            return HttpResponseRedirect('/')
        else:
            return render(request, 'auth/login.html', {'error': 'Неверный логин или пароль', 'categories_menu':categories_menu})
    return render(request, 'auth/login.html', {'categories_menu': categories_menu,})


def reg_view(request):
    categories_menu = Category.objects.all()
    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if password != password2:
            return render(request, 'auth/register.html', {'error':'Пароли не совпадают', 'categories_menu':categories_menu})
        if len(password)<3:
            return render(request, 'auth/register.html', {'error':'Пароль должен быть больше 3 символов', 'categories_menu':categories_menu})
        if password == password2:
            User.objects.create_user(username=login, password=password)
            usr = authenticate(request, username=login, password=password)
            if usr is not None:
                user_login(request, usr)
                return HttpResponseRedirect('/')
            else:
                return render(request, 'auth/register.html', {'error': 'Неверный логин или пароль', 'categories_menu':categories_menu})
    return render(request, 'auth/register.html', {'categories_menu': categories_menu,})


def logout_view(request):
    user_logout(request)
    return HttpResponseRedirect('/')