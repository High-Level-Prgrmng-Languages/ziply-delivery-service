from django.shortcuts import render
from django.http import JsonResponse
from django.db.utils import OperationalError
from django.db import connections


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
