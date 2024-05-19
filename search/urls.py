from django.urls import path
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name = "search"
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('create_ad/', login_required(views.CreateAdView.as_view()), name='create_ad'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
