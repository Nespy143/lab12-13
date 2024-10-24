from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms
from django.contrib.auth import get_user_model
User = get_user_model()

MAX_USERS = 2  # Максимальное количество пользователей в кафе


def home(request):
    if request.user.is_authenticated:
        if request.user.is_present:
            return render(request, 'cafe/home.html', {
                'users': User.objects.filter(is_present=True),
            })
        else:
            return redirect('login')
    else:
        return redirect('login')



def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is None:
            print('Все не правильно')
        else:
            if User.objects.filter(is_present=True).count() < MAX_USERS:
                login(request, user)
                request.user.is_present = True
                request.user.save()
                return redirect('home')
            else:
                return render(request, 'cafe/login.html', {'error': 'Кафе переполнено!'})
    return render(request, 'cafe/login.html')


def register(request):
    if request.method == "GET":
        form = forms.RegisterForm()
        return render(request, 'cafe/register.html', {
            'form': form
        })
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print(326526+5)
            return redirect('login')  # После регистрации перенаправляем на авторизацию
        else:
            form = forms.RegisterForm()
            return render(request, 'cafe/register.html', {'form': form})


@login_required
def order_coffee(request):
    request.user.is_drinking_coffee = True
    request.user.save()
    return redirect('home')


@login_required
def drink_coffee(request):
    request.user.is_drinking_coffee = False
    request.user.save()
    return redirect('home')


@login_required
def leave_cafe(request):
    request.user.is_present = False
    request.user.save()
    logout(request)
    return redirect('home')

