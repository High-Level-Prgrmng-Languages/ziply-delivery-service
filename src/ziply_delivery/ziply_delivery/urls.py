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
    path('', include('client.urls')),
    path('support', views.support, name='support'),
    path('about', views.about, name='support'),
    path('api', include('api.urls')),
    path('company/', include('company.urls')),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
