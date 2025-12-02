"""
Parcels Views - REST API Endpoints
Created: November 29, 2025
Author: Delivery Service Team

This file contains the API views for parcel management.
Provides endpoints for creating, listing, and retrieving parcels.
Uses Django REST Framework for JSON API responses.
"""

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Parcel
from django.utils import timezone

@api_view(['GET', 'POST'])
def parcel_list_create(request):
    """
    Handle both listing all parcels (GET) and creating new parcels (POST)
    
    GET /api/parcels/
    - Returns list of all parcels with basic information
    - Used by admin dashboard to see all parcels
    
    POST /api/parcels/
    - Creates a new parcel in the system
    - Automatically generates tracking number and UUID
    - Initializes status history with 'pending' status
    """
    
    if request.method == 'GET':
        # Retrieve all parcels from MongoDB
        parcels = Parcel.objects.all()
        parcel_data = []
        
        # Convert each parcel to JSON-serializable format
        for parcel in parcels:
            parcel_data.append({
                'id': str(parcel._id),  # Convert ObjectId to string for JSON
                'tracking_number': parcel.tracking_number,
                'sender_name': parcel.sender_name,
                'recipient_name': parcel.recipient_name,
                'current_status': parcel.current_status,
                'current_location_address': parcel.current_location_address,
                'created_at': parcel.created_at.isoformat() if parcel.created_at else None,
                'estimated_delivery': parcel.estimated_delivery.isoformat() if parcel.estimated_delivery else None
            })
        
        return Response(parcel_data)
    
    elif request.method == 'POST':
        """
        Create a new parcel with the provided data
        Expected JSON format:
        {
            "sender_name": "John Doe",
            "recipient_name": "Jane Smith",
            "estimated_delivery": "2025-11-29T10:00:00Z",
            "current_location_address": "Warehouse A"
        }
        """
        try:
            # Create new parcel with initial status history
            parcel = Parcel.objects.create(
                sender_name=request.data.get('sender_name'),
                recipient_name=request.data.get('recipient_name'),
                estimated_delivery=request.data.get('estimated_delivery'),
                current_location_address=request.data.get('current_location_address', ''),
                status_history=[{
                    'status': 'pending',
                    'timestamp': timezone.now(),
                    'notes': 'Parcel created'
                }]
            )
            
            # Return success response with parcel details
            return Response({
                'id': str(parcel._id),
                'tracking_number': parcel.tracking_number,
                'status': parcel.current_status
            }, status=status.HTTP_201_CREATED)
            
        except Exception as e:
            # Return error if parcel creation fails
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_parcel(request, tracking_number):
    """
    Retrieve a specific parcel by its tracking number
    
    GET /api/parcels/{tracking_number}/
    - Returns complete parcel information including status history
    - Used by customers to track their packages
    - Returns 404 if tracking number not found
    """
    try:
        # Find parcel by tracking number
        parcel = Parcel.objects.get(tracking_number=tracking_number)
        
        # Return complete parcel information
        return Response({
            'id': str(parcel._id),
            'tracking_number': parcel.tracking_number,
            'sender_name': parcel.sender_name,
            'recipient_name': parcel.recipient_name,
            'current_status': parcel.current_status,
            'current_location_address': parcel.current_location_address,
            'status_history': parcel.status_history,  # Complete tracking history
            'created_at': parcel.created_at.isoformat() if parcel.created_at else None,
            'estimated_delivery': parcel.estimated_delivery.isoformat() if parcel.estimated_delivery else None
        })
        
    except Parcel.DoesNotExist:
        # Return 404 if tracking number not found
        return Response({'error': 'Parcel not found'}, status=status.HTTP_404_NOT_FOUND)
