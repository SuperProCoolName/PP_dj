from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('user/<int:pk>/', views.UserDetailView.as_view(), name='profile'),
    path('profile_edit/', views.profile_edit, name='profile_edit')
]
