from django.http import JsonResponse
from django.db.utils import OperationalError
from django.shortcuts import redirect, render
from django.db import connections
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as Login


def home(request):
    return render(request, 'home.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        print(username)
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            Login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Password or username invalid'})
    else:
        return render(request, 'login.html')


def support(request):
    return render(request, 'support.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        # TODO: phone = request.POST.get('phone')
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
