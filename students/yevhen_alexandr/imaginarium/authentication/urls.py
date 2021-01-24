from django.contrib.auth import views
from django.urls import path
from .views import RegistrationView

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', RegistrationView.as_view(), name='register')
]