from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, authenticate
from django.views import generic
from django.urls import reverse_lazy
from .models import Ad
from .forms import CreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.db.models.functions import Lower

# Create your views here.


class HomeView(generic.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Получаем 5 последних объявлений
        latest_ads = Ad.objects.order_by('-created_at')[:10]
        context['latest_ads'] = latest_ads
        return context

class AboutView(generic.TemplateView):
    template_name = 'about.html'

class SecurityView(generic.TemplateView):
    template_name = 'security.html' 

class Article1View(generic.TemplateView):
    template_name = 'article1.html' 

class Article2View(generic.TemplateView):
    template_name = 'article2.html' 

class IndexView(generic.ListView):
    template_name = 'search/index.html'
    context_object_name = 'ad_list'

    def get_queryset(self):
        queryset = Ad.objects.all()

        quick_search = self.request.GET.get('quick_search')

        if quick_search:
            quick_search = quick_search.lower()
            queryset = queryset.filter(
                Q(title__icontains=quick_search) |
                Q(description__icontains=quick_search)
            )

        # Получаем параметры из GET запроса
        min_price = self.request.GET.get('price_from')
        max_price = self.request.GET.get('price_to')
        # source = self.request.GET.get('source')
        # condition = self.request.GET.getlist('condition')
        # author = self.request.GET.get('author')
        # certification = self.request.GET.get('certification')
        description = self.request.GET.get('description')
        title_only = self.request.GET.get('title_only')
        # Применяем фильтры
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
        # if source:
        #     queryset = queryset.filter(source__icontains=source)
        # if condition:
        #     queryset = queryset.filter(condition__in=condition)
        # if author:
        #     queryset = queryset.filter(author__icontains=author)
        # if certification:
        #     queryset = queryset.filter(certification=certification)
        if description:
            description = description.lower()
            if title_only:
                queryset = queryset.filter(title__icontains=description)
            else:
                queryset = queryset.filter(
                    Q(description__icontains=description) |
                    Q(title__icontains=description)
                )

        return queryset


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
