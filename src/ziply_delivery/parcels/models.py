"""
Parcels Models - MongoDB Document Definitions
Created: November 29, 2025
Author: Delivery Service Team

This file defines the data models for the parcel tracking system using Django with MongoDB.
We use Djongo to bridge Django ORM with MongoDB's document-based storage.
"""

import uuid
from django.db import models
from djongo import models as djongo_models


def generate_uuid():
    """
    Generate a unique UUID string for parcel identification
    Returns: String representation of UUID4
    """
    return str(uuid.uuid4())


class Address(djongo_models.Model):
    """
    Embedded document for storing address information
    Used for both sender and recipient addresses
    Abstract model - will not create its own collection
    """
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=20)
    country = models.CharField(max_length=100)

    class Meta:
        abstract = True  # This makes it an embedded document


class StatusHistory(djongo_models.Model):
    """
    Embedded document for tracking parcel status changes
    Stores the complete journey of a parcel
    Abstract model - embedded in Parcel document
    """
    status = models.CharField(max_length=50)
    location = models.CharField(max_length=255)
    timestamp = models.DateTimeField()
    notes = models.TextField(blank=True)

    class Meta:
        abstract = True  # This makes it an embedded document


class Parcel(models.Model):
    """
    Main Parcel document stored in MongoDB
    Represents a package being tracked through the delivery system
    Uses embedded documents for addresses and status history
    """

    # Status choices for parcel tracking
    STATUS_CHOICES = [
        ('pending', 'Pending'),      # Just created, not yet picked up
        ('in_transit', 'In Transit'),  # On the way to destination
        ('delivered', 'Delivered'),   # Successfully delivered
        ('failed', 'Failed'),        # Delivery failed
    ]

    # Primary key - custom UUID instead of MongoDB ObjectId
    _id = models.CharField(
        max_length=36, primary_key=True, default=generate_uuid)

    # Unique tracking number for customer reference
    tracking_number = models.CharField(max_length=100, unique=True)

    # Sender information
    sender_name = models.CharField(max_length=255)
    sender_address = djongo_models.EmbeddedModelField(model_container=Address)

    # Recipient information
    recipient_name = models.CharField(max_length=255)
    recipient_address = djongo_models.EmbeddedModelField(
        model_container=Address)

    # Current status and location
    current_status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='pending')
    current_location_lat = models.FloatField(
        null=True, blank=True)  # GPS latitude
    current_location_lng = models.FloatField(
        null=True, blank=True)  # GPS longitude
    current_location_address = models.CharField(
        max_length=255, blank=True)  # Human-readable address

    # Timestamps
    created_at = models.DateTimeField(
        auto_now_add=True)  # When parcel was created
    estimated_delivery = models.DateTimeField(
        null=True, blank=True)  # Expected delivery time

    # Status history - array of embedded documents
    status_history = djongo_models.ArrayModelField(
        model_container=StatusHistory, default=list)

    class Meta:
        db_table = 'parcels'  # MongoDB collection name
        ordering = ['-created_at']  # Newest first
