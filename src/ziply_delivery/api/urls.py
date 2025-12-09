"""
Main API URL Configuration
Created: November 29, 2025
Author: Delivery Service Team

API URL configuration for the entire Django project.
Includes API endpoints, admin interface, and health checks.
"""

from django.urls import path
from . import views

# URL patterns for the api
urlpatterns = [
    path('parcels/', views.ParcelListCreateView.as_view(), name='parcel-list-create'),
    path('parcels/<str:tracking_number>/', views.ParcelDetailView.as_view(), name='parcel-detail'),
    path('parcels/<str:tracking_number>/update-status/', views.UpdateParcelStatusView.as_view(), name='update-parcel-status'),
    path('health/', views.health_check, name='health-check'),
]
