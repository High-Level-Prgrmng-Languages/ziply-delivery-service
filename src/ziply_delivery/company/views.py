from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as Login
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required


def package(request):
    return render(request, 'package.html')


@login_required
def register(request):
    if request.method == 'POST':
        # user is logged in
        email = request.POST.get('email')
        company = request.POST.get('company')
        # TODO: zip = request.POST.get('zip')
        # TODO: phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

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

        # TODO: Store phone
        # TODO: new_company = Company(company, )
        group = Group.objects.get_or_create(name=company)
        request.user.groups.add(group)
        return redirect('home')
    else:
        return render(request, 'register.html', {'isCompany': 'True'})
