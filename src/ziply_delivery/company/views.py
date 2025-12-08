from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as Login
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required
from .models import Company

from rest_framework.test import APIClient


@login_required(login_url='login')
def parcel_create(request):
    if request.method == 'POST':
        # find parcel
        tracking_number = request.POST.get('tracking_number')

        sender_name = request.POST.get('sender_name')
        recipient_name = request.POST.get('recipient_name')
        estimated_delivery = request.POST.get('estimated_delivery')
        current_location_address = request.POST.get(
            'current_location_address')

        client = APIClient()
        response = client.post('api/',
                               {
                                   "sender_name": sender_name,
                                   "recipient_name": recipient_name,
                                   "estimated_delivery": estimated_delivery,
                                   "current_location_address": current_location_address
                               }, format='json')
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
