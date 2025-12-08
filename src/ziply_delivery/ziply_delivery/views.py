"""
Main Project Views
Created: Dec 7th, 2025
Author: Delivery Service Team

The main views of home and support page
"""


from django.shortcuts import render, redirect


def home(request):
    """
    Home page
    """
    return render(request, 'home.html')


def support(request):
    """
    Support page rendering
    """
    return render(request, 'support.html')


def about(request):
    """
    About us page rendering
    """
    return render(request, 'about.html')
