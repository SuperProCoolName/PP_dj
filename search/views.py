from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, authenticate
from django.views import generic
from django.urls import reverse_lazy
from .models import Ad
from .forms import CreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

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


class CreateAdView(LoginRequiredMixin, generic.CreateView):
    model = Ad
    form_class = CreationForm
    template_name = "search/create_ad.html"

    def post(self, request):
        """
        Gets data from the form and saves it to the database.
        """
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.user = request.user
            ad.save()
            # Перенаправление после успешного сохранения
            return redirect('search:detail', pk=ad.pk)
        return render(request, self.template_name, {'form': form})

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DeleteAdView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Ad
    success_url = reverse_lazy('search:index')
    template_name = "search/delete_ad.html"

    def test_func(self):
        ad = self.get_object()
        return self.request.user == ad.user


class UpdateAdView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Ad
    form_class = CreationForm
    template_name = 'search/update_ad.html'

    def test_func(self):
        ad = self.get_object()
        return self.request.user == ad.user

    def form_valid(self, form):
        ad = form.save()
        return redirect(reverse_lazy('search:detail', kwargs={'pk': ad.pk}))
