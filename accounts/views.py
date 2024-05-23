from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect

# Create your views here.


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class LogoutView(generic.View):
    def get(self, request):
        return render(request, 'registration/logout_confirm.html')

    def post(self, request):
        logout(request)
        return redirect('home')
