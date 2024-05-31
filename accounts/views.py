from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, login
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from .forms import UserLoginForm
from django.contrib.auth.models import User
from search.models import Ad
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


class UserDetailView(generic.DetailView):
    model = User
    template_name = 'accounts/profile.html'
    context_object_name = 'user'

    def get_object(self):
        return User.objects.get(pk=self.kwargs.get('pk'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context["user_ads"] = Ad.objects.filter(user=user)
        return context
