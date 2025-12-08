"""
Main API URL Configuration
Created: November 29, 2025
Author: Delivery Service Team

API URL configuration for the entire Django project.
Includes API endpoints, admin interface, and health checks.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

# URL patterns for the api
urlpatterns = [
    path('health/', views.health_check,
         name='health-check'),     # Health monitoring
    # Parcel tracking API
    path('parcels/', include('parcels.urls')),
    # Pages management API
    path('pages/', include('pages.urls')),
]
