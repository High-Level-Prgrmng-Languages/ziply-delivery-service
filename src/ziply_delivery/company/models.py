"""
Company Models
Created: Dec 7th, 2025
Author: Delivery Service Team

The main models for company accounts
"""

from django.db import models


class Company(models.Model):
    # Company name
    name = models.CharField(max_length=200, unique=True)

    # Company address in full
    address = models.TextField()

    # Zip code
    zipcode = models.CharField(max_length=10)

    # telephone number
    telephone = models.CharField(max_length=20)

    # Company Email
    email = models.EmailField(unique=True)

    # The associated UUID of the user who created the company
    account = models.CharField(max_length=50, unique=True)

    # Optional improvements
    created_at = models.DateTimeField(
        auto_now_add=True)  # set once when created
    updated_at = models.DateTimeField(auto_now=True)      # updates every save
