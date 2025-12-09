"""
Main Project URL Configuration
Created: November 29, 2025
Author: Delivery Service Team

Root URL configuration for the entire Django project.
Includes API endpoints, admin interface, and health checks.
"""

from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

# URL patterns for the entire application
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('support/', views.support, name='support'),
    path('about/', views.about, name='about'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('terms-of-service/', views.terms_of_service, name='terms_of_service'),
    path('create/', views.create_parcel, name='create_parcel'),
    path('track/', views.track_parcel, name='track_parcel'),
    path('api/', include('api.urls')),  # Include API URLs
    path('api/parcels/', include('parcels.urls')),  # Include parcels API URLs
    path('company/', include('company.urls')),
    path('client/', include('client.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
