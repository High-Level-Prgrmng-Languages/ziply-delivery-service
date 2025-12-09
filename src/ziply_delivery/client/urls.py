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
    path('login/', views.login_select, name='login_select'),
    path('login/', views.login_select, name='login'),  # Add this for compatibility
    path('login/user/', views.user_login, name='user_login'),
    path('login/company/', views.company_login, name='company_login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
]
