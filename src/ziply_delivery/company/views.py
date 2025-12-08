from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as Login
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required
from .models import Company

from ziply_delivery.parcels.models import Parcel
from ziply_delivery.parcels.utils import validate_name, validate_status, validate_address, validate_date
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


@login_required(login_url='login')
def package(request, company_name):
    # if user in that company
    if request.user.groups.filter(name=company_name).exists():
        return render(request, '')


@login_required(login_url='login')
def register(request):
    if request.method == 'POST':
        # user is logged in
        email = request.POST.get('email')
        company = request.POST.get('company')
        zip = request.POST.get('zip')
        telephone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # ------------------- CHECKS
        # check if company exists
        company_exists = Group.objects.filter(name=company)
        if company_exists:
            return render(request, 'register.html', {'error': 'Company already Exists', 'isCompany': 'True'})

        # TODO: add more checks
        if not email or not password:
            return render(request, 'register.html', {'error': 'Missing username or password', 'isCompany': 'True'})
            return render(request, 'register.html', {'error': 'Email and password required'})

        # check password matches
        if password != confirm_password:
            return render(request, 'register.html', {'error': 'Passwords do not match', 'isCompany': 'True'})

        # -------------------- CREATION
        group = Group.objects.get_or_create(name=company)
        new_company = Company(name=company, zipcode=zip,
                              telephone=telephone, email=email, account=request.user.id)
        new_company.save()
        request.user.groups.add(group)
        return redirect('home')
    else:
        return render(request, 'register.html', {'isCompany': 'True'})
