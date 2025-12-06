"""
Main Project URL Configuration
Created: November 29, 2025
Author: Delivery Service Team

Root URL configuration for the entire Django project.
Includes API endpoints, admin interface, and health checks.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

# URL patterns for the entire application
urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('support', views.support, name='support'),
    # Root endpoint
    path('api', views.api_root, name='api-root'),
    path('company/', include('company.urls')),
    path('health/', views.health_check,
         name='health-check'),     # Health monitoring
    # Django admin interface
    path('admin/', admin.site.urls),
    # Parcel tracking API
    path('api/parcels/', include('parcels.urls')),
    # Pages management API
    path('api/pages/', include('pages.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
