"""
Parcels Views - Endpoints
Created: December 7th, 2025
Author: Delivery Service Team

This file contains the views for parcel management.
Provides views for creating, listing, and retrieving parcels.
"""

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as Login
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required
from .models import Parcel
from .utils import validate_name, validate_status, validate_address, validate_date
from ziply_delivery.parcels.models import generate_uuid
from rest_framework.test import APIClient


@login_required(login_url='login')
def parcel_put(request):
    if request.method == 'POST':

        # find parcel
        parcel = Parcel.objects.get(tracking_number=tracking_number)

        # --------------validations
        sender_name = validate_name(
            request.POST.get('sender_name'), parcel.sender_name)
        recipient_name = validate_name(request.POST.get(
            'recipient_name'), parcel.recipient_name)
        current_status = validate_status(request.POST.get(
            'current_status'), parcel.current_status)
        current_location_address = validate_address(request.POST.get(
            'current_location_address'), parcel.current_location_address)
        estimated_delivery = validate_date(request.POST.get(
            'estimated_delivery'), parcel.estimated_delivery)

        created_at = parcel.created_at
        status_history = parcel.status_history

        client = APIClient()
        response = client.post('api/', {
            'id': generate_uuid(),
            'tracking_number': generate_uuid(),
            'sender_name': sender_name,
            'recipient_name': recipient_name,
            'current_status': current_status,
            'current_location_address': current_location_address,
            'status_history': status_history,
            'created_at': created_at,
            'estimated_delivery': estimated_delivery,
        }, format='json')
        # ------------------- CHECKS
    else:
        return redirect('404')


@ login_required(login_url='login')
def get_parcel(request, tracking_number):
    if request.method == 'POST':
