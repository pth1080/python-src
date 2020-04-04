from django.urls import path

from src.users import views

urlpatterns = [
    path('sign-up/', views.UserRegisterView.as_view())
]
