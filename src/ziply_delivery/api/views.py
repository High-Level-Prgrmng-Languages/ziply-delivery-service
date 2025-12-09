from django.shortcuts import render
from django.http import JsonResponse
from django.db.utils import OperationalError
from django.db import connections
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json


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


@method_decorator(csrf_exempt, name='dispatch')
class UpdateParcelStatusView(View):
    def post(self, request, tracking_number):
        try:
            from parcels.models import Parcel
            parcel = Parcel.objects.get(tracking_number=tracking_number)
            data = json.loads(request.body)
            
            # Add new status update
            parcel.add_status_update(
                status=data.get('status'),
                location=data.get('location', ''),
                notes=data.get('notes', '')
            )
            
            return JsonResponse({'success': True, 'message': 'Status updated successfully'})
        except Parcel.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Parcel not found'}, status=404)
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=500)


class ParcelListCreateView(View):
    def get(self, request):
        """List all parcels"""
        try:
            from parcels.models import Parcel
            parcels = Parcel.objects.all()
            parcel_data = []
            
            for parcel in parcels:
                parcel_data.append({
                    'tracking_number': parcel.tracking_number,
                    'sender_name': parcel.sender_name,
                    'recipient_name': parcel.recipient_name,
                    'current_status': parcel.current_status,
                    'created_at': parcel.created_at.isoformat() if parcel.created_at else None,
                    'estimated_delivery': parcel.estimated_delivery.isoformat() if parcel.estimated_delivery else None
                })
            
            return JsonResponse({'parcels': parcel_data})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    def post(self, request):
        """Create a new parcel"""
        try:
            from parcels.models import Parcel
            data = json.loads(request.body)
            
            parcel = Parcel.objects.create(
                sender_name=data.get('sender_name'),
                sender_address=data.get('sender_address', ''),
                recipient_name=data.get('recipient_name'),
                recipient_address=data.get('recipient_address', ''),
                package_contents=data.get('package_contents', ''),
                package_weight=data.get('package_weight'),
                current_location_address=data.get('current_location_address', '')
            )
            
            return JsonResponse({
                'success': True,
                'tracking_number': parcel.tracking_number,
                'message': 'Parcel created successfully'
            })
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)


class ParcelDetailView(View):
    def get(self, request, tracking_number):
        """Get specific parcel details"""
        try:
            from parcels.models import Parcel
            parcel = Parcel.objects.get(tracking_number=tracking_number)
            
            parcel_data = {
                'tracking_number': parcel.tracking_number,
                'sender_name': parcel.sender_name,
                'sender_address': parcel.sender_address,
                'recipient_name': parcel.recipient_name,
                'recipient_address': parcel.recipient_address,
                'package_contents': parcel.package_contents,
                'package_weight': str(parcel.package_weight) if parcel.package_weight else None,
                'current_status': parcel.current_status,
                'current_location_address': parcel.current_location_address,
                'created_at': parcel.created_at.isoformat() if parcel.created_at else None,
                'estimated_delivery': parcel.estimated_delivery.isoformat() if parcel.estimated_delivery else None,
                'status_history': json.loads(parcel.status_history) if parcel.status_history else []
            }
            
            return JsonResponse(parcel_data)
        except Parcel.DoesNotExist:
            return JsonResponse({'error': 'Parcel not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
