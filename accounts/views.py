from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, login
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from .forms import UserLoginForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView

# Create your views here.


def signup_view(request):
    if request.method == 'POST':
        # Получаем данные из POST-запроса
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Создаем нового пользователя
        user = User.objects.create_user(username=username, password=password)

        # Выполняем вход для нового пользователя
        login(request, user)

        # Перенаправляем на другую страницу после успешной регистрации
        return redirect('home')

    # Если это GET-запрос, отображаем форму регистрации
    return render(request, 'registration/signup.html')


class LogoutView(generic.View):
    def get(self, request):
        return render(request, 'registration/logout_confirm.html')

    def post(self, request):
        logout(request)
        return redirect('home')


class LoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'registration/login.html'
