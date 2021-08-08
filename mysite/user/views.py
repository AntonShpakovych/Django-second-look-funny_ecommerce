from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from user.forms import UserLoginForm, UserRegisterForm
from django.contrib.auth import login, logout


def logout_user(request):
    logout(request)
    return redirect('login_user')


def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = UserLoginForm()
    return render(request, 'user/user_login.html', {'form': form})


def register_user(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congratulation')
            return redirect('login_user')
        else:
            messages.error(request, 'Error data, change login or password')
    else:
        form = UserRegisterForm()

    return render(request, 'user/user_register.html', {'form': form})
