"""
Main Project URL Configuration
Created: November 29, 2025
Author: Delivery Service Team

Root URL configuration for the entire Django project.
Includes API endpoints, admin interface, and health checks.
"""

from django.contrib import admin
from django.contrib.auth import login as Login
from django.urls import path, include
from django.http import JsonResponse
from django.db import connections
from django.db.utils import OperationalError
from django.shortcuts import redirect, render
from django.contrib.auth.models import User


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # TODO: add more checks
        if not email or not password:
            return render(request, 'register.html', {'error': 'Email and passord required'})

        # TODO: Store phone
        user = User.objects.create_user(username=username,
                                        email=email, first_name=first_name, last_name=last_name, password=password)
        Login(request, user)
        return redirect('home')
    else:
        return render(request, 'register.html')


def api_root(request):
    """
    Root API endpoint - provides welcome message and available endpoints
    Helps developers discover the API structure
    """
    return JsonResponse({
        'message': 'Welcome to NoSQL Library API',
        'version': '1.0.0',
        'date': 'November 29, 2025',
        'endpoints': {
            'parcels': '/api/parcels/',
            'pages': '/api/pages/',
            'admin': '/admin/',
            'health': '/health/'
        }
    })


def health_check(request):
    """
    Health check endpoint for monitoring system status
    Tests database connectivity and returns system information
    Used by monitoring tools and load balancers
    """
    try:
        # Test MongoDB connection through Djongo
        db_conn = connections['default']
        db_conn.ensure_connection()

        # Test with a simple query
        from parcels.models import Parcel
        parcel_count = Parcel.objects.count()

        return JsonResponse({
            'status': 'healthy',
            'database': 'connected',
            'mongodb_engine': 'djongo',
            'timestamp': '2025-11-29',
            'collections': {
                'parcels': parcel_count,
                'pages': 'available'
            }
        })

    except OperationalError as e:
        return JsonResponse({
            'status': 'unhealthy',
            'database': 'disconnected',
            'error': str(e),
            'timestamp': '2025-11-29'
        }, status=500)

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'database': 'unknown',
            'error': str(e),
            'timestamp': '2025-11-29'
        }, status=500)


# URL patterns for the entire application
urlpatterns = [
    path('', home, name='home'),
    path('register', register, name='register'),
    path('api', api_root, name='api-root'),                    # Root endpoint
    path('company/', include('company.urls')),
    path('health/', health_check, name='health-check'),     # Health monitoring
    # Django admin interface
    path('admin/', admin.site.urls),
    # Parcel tracking API
    path('api/parcels/', include('parcels.urls')),
    # Pages management API
    path('api/pages/', include('pages.urls')),
]
