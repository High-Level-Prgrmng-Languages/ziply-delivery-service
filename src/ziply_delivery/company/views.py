from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.utils import timezone
from django.utils.dateparse import parse_datetime

def register(request):
    if request.method == 'POST':
        # Handle company registration
        username = request.POST.get('username')
        password = request.POST.get('password')
        company_name = request.POST.get('company_name')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return render(request, 'company/register.html')
        
        # Create user and company group
        user = User.objects.create_user(username=username, password=password)
        group, created = Group.objects.get_or_create(name=company_name)
        user.groups.add(group)
        
        messages.success(request, 'Company registered successfully')
        return redirect('login')
    
    return render(request, 'company/register.html')

@login_required(login_url='login')
def package(request, company_name):
    if request.user.groups.filter(name=company_name).exists():
        from parcels.models import Parcel
        # Get parcels created by this company (you might need to add a company field to Parcel model)
        parcels = Parcel.objects.all().order_by('-created_at')  # For now, show all parcels
        return render(request, 'company/dashboard.html', {
            'company_name': company_name,
            'parcels': parcels
        })
    else:
        messages.error(request, 'Access denied')
        return redirect('login')

@login_required(login_url='login')
def parcel_create(request, company_name):
    if request.user.groups.filter(name=company_name).exists():
        if request.method == 'POST':
            # Handle parcel creation
            from parcels.models import Parcel
            from django.utils import timezone
            from django.utils.dateparse import parse_datetime
            
            try:
                # Parse and make timezone-aware
                estimated_delivery_str = request.POST.get('estimated_delivery')
                estimated_delivery = None
                if estimated_delivery_str:
                    estimated_delivery = parse_datetime(estimated_delivery_str)
                    if estimated_delivery and timezone.is_naive(estimated_delivery):
                        estimated_delivery = timezone.make_aware(estimated_delivery)

                parcel = Parcel.objects.create(
                    sender_name=request.POST.get('sender_name'),
                    sender_address=request.POST.get('sender_address'),
                    recipient_name=request.POST.get('recipient_name'),
                    recipient_address=request.POST.get('recipient_address'),
                    package_contents=request.POST.get('package_contents'),
                    package_weight=request.POST.get('package_weight'),
                    estimated_delivery=estimated_delivery,
                    current_location_address=request.POST.get('current_location_address', ''),
                    status_history=[{
                        'status': 'pending',
                        'timestamp': timezone.now(),
                        'location': request.POST.get('current_location_address', ''),
                        'notes': f'Parcel created by {company_name}'
                    }]
                )
                messages.success(request, f'Parcel created successfully! Tracking number: {parcel.tracking_number}')
                return redirect('company_dashboard', company_name=company_name)
            except Exception as e:
                messages.error(request, f'Error creating parcel: {str(e)}')
        
        return render(request, 'company/create_parcel.html', {'company_name': company_name})
    else:
        messages.error(request, 'Access denied')
        return redirect('login')
