"""
Main Project URL Configuration
Created: November 29, 2025
Author: Delivery Service Team

Root URL configuration for the entire Django project.
Includes API endpoints, admin interface, and health checks.
"""
from django.urls import path
from . import views

# URL patterns for the client app
urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
]
