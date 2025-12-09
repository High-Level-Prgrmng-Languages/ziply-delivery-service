from django.shortcuts import redirect, render
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login as Login, logout as Logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def login_select(request):
    """
    Login type selection page
    """
    return render(request, 'login_select.html')

def user_login(request):
    """
    User login page - for customers who can only track
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Check if user is NOT part of any company group
            if not user.groups.exists():
                Login(request, user)
                return redirect('home')
            else:
                return render(request, 'user_login.html', {
                    'error': 'This account is registered as a company. Please use company login.'
                })
        else:
            return render(request, 'user_login.html', {
                'error': 'Invalid username or password'
            })
    
    return render(request, 'user_login.html')

def company_login(request):
    """
    Company login page - for companies who can create shipments
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Check if user is part of a company group
            if user.groups.exists():
                Login(request, user)
                return redirect('home')
            else:
                return render(request, 'company_login.html', {
                    'error': 'This account is not registered as a company. Please use user login.'
                })
        else:
            return render(request, 'company_login.html', {
                'error': 'Invalid username or password'
            })
    
    return render(request, 'company_login.html')

# Keep existing login function as fallback
def login(request):
    """
    Redirect to login selection
    """
    return redirect('login_select')

@login_required
def logout(request):
    """
    Logout user and redirect to home
    """
    Logout(request)
    return redirect('home')

def register(request):
    """
    Register page rendering
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email', '')
        
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already exists'})
        
        user = User.objects.create_user(username=username, password=password, email=email)
        Login(request, user)
        return redirect('home')
    
    return render(request, 'register.html')
