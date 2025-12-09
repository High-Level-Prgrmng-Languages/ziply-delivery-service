from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as Login, logout as Logout
from django.contrib.auth.decorators import login_required
from .models import Customer


def login(request):
    """
    Login page rendering
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            Login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Password or username invalid'})
    else:
        return render(request, 'login.html')

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
