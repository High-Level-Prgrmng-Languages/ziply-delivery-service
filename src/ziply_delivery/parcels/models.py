"""
Parcels Models - Simplified for SQLite compatibility
Created: November 29, 2025
Author: Delivery Service Team
"""

import uuid
import random
import string
import json
from django.db import models


def generate_uuid():
    """
    Generate a unique UUID string for parcel identification
    Returns: String representation of UUID4
    """
    return str(uuid.uuid4())


def generate_tracking_number():
    """
    Generate a unique tracking number in format TRK + 9 random alphanumeric characters
    Returns: String like 'TRK123ABC456'
    """
    chars = string.ascii_uppercase + string.digits
    random_part = ''.join(random.choices(chars, k=9))
    return f'TRK{random_part}'


class Parcel(models.Model):
    """
    Main Parcel model - simplified for SQLite compatibility
    """

    # Status choices for parcel tracking
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_transit', 'In Transit'),
        ('delivered', 'Delivered'),
        ('failed', 'Failed'),
    ]

    # Primary key - custom UUID
    _id = models.CharField(max_length=36, primary_key=True, default=generate_uuid)

    # Unique tracking number for customer reference
    tracking_number = models.CharField(max_length=100, unique=True, default=generate_tracking_number)

    # Sender information (simplified)
    sender_name = models.CharField(max_length=255)
    sender_address = models.TextField(blank=True)  # JSON string for address

    # Recipient information (simplified)
    recipient_name = models.CharField(max_length=255)
    recipient_address = models.TextField(blank=True)  # JSON string for address

    # Current status and location
    current_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    current_location_lat = models.FloatField(null=True, blank=True)
    current_location_lng = models.FloatField(null=True, blank=True)
    current_location_address = models.CharField(max_length=255, blank=True)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    estimated_delivery = models.DateTimeField(null=True, blank=True)

    # Status history as JSON field
    status_history = models.TextField(default='[]')  # JSON string for status history

    class Meta:
        db_table = 'parcels'
        ordering = ['-created_at']

    def get_status_history(self):
        """Return status history as Python list"""
        try:
            return json.loads(self.status_history)
        except:
            return []

    def set_status_history(self, history_list):
        """Set status history from Python list"""
        self.status_history = json.dumps(history_list, default=str)

    def add_status_update(self, status, location='', notes=''):
        """Add a new status update to history"""
        from django.utils import timezone
        
        history = self.get_status_history()
        history.append({
            'status': status,
            'timestamp': timezone.now().isoformat(),
            'location': location,
            'notes': notes
        })
        self.set_status_history(history)
        self.current_status = status
        self.save()

    def __str__(self):
        return f"Parcel {self.tracking_number}"
