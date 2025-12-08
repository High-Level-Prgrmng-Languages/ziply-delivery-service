from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as Login
from models import Customer


def login(request):
    """
    Login page rendering
    """
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


def register(request):
    """
    Creates a new customer and user
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        telephone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # ---------------------- CHECKS
        if password != confirm_password:
            return render(request, 'register.html', {'error': 'Passwords do not match'})

        if not email or not password:
            return render(request, 'register.html', {'error': 'Email and password required'})

        user_exists = User.objects.filter(username=username)
        if (user_exists):
            return render(request, 'register.html', {'error': 'User already exists'})

        # ---------------------- CREATION
        user = User.objects.create_user(username=username,
                                        email=email, first_name=first_name, last_name=last_name, password=password)
        new_customer = Customer(first_name=first_name, last_name=last_name,
                                telephone=telephone, account=user.id(), email=email)
        new_customer.save()
        Login(request, user)
        return redirect('home')
    else:
        return render(request, 'register.html')
