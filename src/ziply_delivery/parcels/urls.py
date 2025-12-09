"""
Parcels URL Configuration
Created: November 29, 2025
Author: Delivery Service Team

Defines URL patterns for the parcels API endpoints.
Maps URLs to their corresponding view functions.
"""

from django.urls import path
from . import views
from api.views import UpdateParcelStatusView

urlpatterns = [
    # /api/parcels/ - List all parcels (GET) or create new parcel (POST)
    path('', views.parcel_list_create, name='parcel-list-create'),

    # /api/parcels/{tracking_number}/ - Get specific parcel by tracking number
    path('<str:tracking_number>/', views.get_parcel, name='get_parcel'),
    
    # /api/parcels/{tracking_number}/update-status/ - Update parcel status
    path('<str:tracking_number>/update-status/', UpdateParcelStatusView.as_view(), name='update-parcel-status'),
]
