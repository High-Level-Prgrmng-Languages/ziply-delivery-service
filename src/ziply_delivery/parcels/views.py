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
import json


@api_view(['GET', 'POST'])
def parcel_list_create(request):
    """
    Handle both listing all parcels (GET) and creating new parcels (POST)
    """

    if request.method == 'GET':
        parcels = Parcel.objects.all()
        parcel_data = []

        for parcel in parcels:
            parcel_data.append({
                'id': str(parcel._id),
                'tracking_number': parcel.tracking_number,
                'sender_name': parcel.sender_name,
                'recipient_name': parcel.recipient_name,
                'current_status': parcel.current_status,
                'current_location_address': parcel.current_location_address,
                'created_at': parcel.created_at.isoformat() if parcel.created_at else None,
                'estimated_delivery': parcel.estimated_delivery.isoformat() if parcel.estimated_delivery else None,
                'status_history': parcel.get_status_history()
            })

        return Response(parcel_data)

    elif request.method == 'POST':
        try:
            # Create initial status history
            initial_history = [{
                'status': 'pending',
                'timestamp': timezone.now().isoformat(),
                'location': request.data.get('current_location_address', ''),
                'notes': 'Parcel created and ready for pickup'
            }]

            # Create new parcel
            parcel = Parcel.objects.create(
                sender_name=request.data.get('sender_name'),
                sender_address=request.data.get('sender_address'),
                recipient_name=request.data.get('recipient_name'),
                recipient_address=request.data.get('recipient_address'),
                estimated_delivery=request.data.get('estimated_delivery'),
                current_location_address=request.data.get('current_location_address', ''),
                status_history=json.dumps(initial_history, default=str)
            )

            return Response({
                'id': str(parcel._id),
                'tracking_number': parcel.tracking_number,
                'status': parcel.current_status,
                'message': f'Parcel created successfully! Tracking number: {parcel.tracking_number}'
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_parcel(request, tracking_number):
    """
    Retrieve a specific parcel by tracking number
    """
    try:
        parcel = Parcel.objects.get(tracking_number=tracking_number)
        
        parcel_data = {
            'id': str(parcel._id),
            'tracking_number': parcel.tracking_number,
            'sender_name': parcel.sender_name,
            'recipient_name': parcel.recipient_name,
            'current_status': parcel.current_status,
            'current_location_address': parcel.current_location_address,
            'created_at': parcel.created_at.isoformat() if parcel.created_at else None,
            'estimated_delivery': parcel.estimated_delivery.isoformat() if parcel.estimated_delivery else None,
            'status_history': parcel.get_status_history()
        }
        
        return Response(parcel_data)
        
    except Parcel.DoesNotExist:
        return Response({'error': 'Parcel not found'}, status=status.HTTP_404_NOT_FOUND)
