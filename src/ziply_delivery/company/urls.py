from django.urls import path
from . import views

urlpatterns = [
    path('<str:company_name>/', views.package, name='company'),
    path('register', views.register, name='register')
]
