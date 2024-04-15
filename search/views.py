from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, authenticate
from django.views import generic
from .models import Ad

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'search/index.html'
    context_object_name = 'ad_list'

    def get_queryset(self):
        return Ad.objects.all()


class DetailView(generic.DetailView):
    model = Ad
    template_name = 'search/detail.html'
    context_object_name = 'ad'


class LoginView(generic.ListView):
    template_name = 'search/login.html'
    context_object_name = 'ad_list'
