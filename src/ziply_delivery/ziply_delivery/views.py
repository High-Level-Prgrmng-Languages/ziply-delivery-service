"""
Main Project Views
Created: Dec 7th, 2025
Author: Delivery Service Team

The main views of home and support page
"""


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils import timezone
from django.contrib import messages

def home(request):
    """
    Home page rendering
    """
    return render(request, 'home.html')


def support(request):
    """
    Support page rendering
    """
    return render(request, 'support.html')


def about(request):
    """
    About page rendering
    """
    return render(request, 'about.html')


def privacy_policy(request):
    """
    Privacy Policy page rendering
    """
    return render(request, 'privacy-policy.html')


def terms_of_service(request):
    """
    Terms of Service page rendering
    """
    return render(request, 'terms-of-service.html')


@login_required(login_url='login')
def create_parcel(request):
    """
    Create parcel page rendering
    """
    if request.method == 'POST':
        from parcels.models import Parcel
        from django.utils import timezone
        from django.contrib import messages
        import json
        
        try:
            # Create initial status history
            initial_history = [{
                'status': 'pending',
                'timestamp': timezone.now().isoformat(),
                'location': request.POST.get('current_location_address', ''),
                'notes': 'Parcel created and ready for pickup'
            }]

            parcel = Parcel.objects.create(
                sender_name=request.POST.get('sender_name'),
                sender_address=request.POST.get('sender_address'),
                recipient_name=request.POST.get('recipient_name'),
                recipient_address=request.POST.get('recipient_address'),
                estimated_delivery=request.POST.get('estimated_delivery'),
                current_location_address=request.POST.get('current_location_address', ''),
                status_history=json.dumps(initial_history, default=str)
            )
            
            # Add success message with tracking number
            messages.success(request, f'Parcel created successfully! Your tracking number is: {parcel.tracking_number}')
            
            # Redirect to track page with the tracking number in session
            request.session['new_tracking_number'] = parcel.tracking_number
            return redirect('track_parcel')
            
        except Exception as e:
            messages.error(request, f'Error creating parcel: {str(e)}')
    
    return render(request, 'create_parcel.html')


def track_parcel(request):
    """
    Track parcel page rendering - no login required for tracking
    """
    # Get the new tracking number from session if available
    new_tracking_number = request.session.pop('new_tracking_number', None)
    
    context = {}
    if new_tracking_number:
        context['new_tracking_number'] = new_tracking_number
        context['show_success'] = True
    
    return render(request, 'track_parcel.html', context)
