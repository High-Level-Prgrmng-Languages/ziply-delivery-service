"""
Database Initialization Management Command
Created: November 29, 2025
Author: Delivery Service Team

Django management command to initialize MongoDB with proper indexes.
Run with: python manage.py init_database

This command creates optimized indexes for:
- Fast parcel lookups by tracking number
- Efficient status and date-based queries
- Geographic queries for delivery optimization
"""

from django.core.management.base import BaseCommand
import pymongo
import os

class Command(BaseCommand):
    help = 'Initialize MongoDB database with optimized indexes for delivery service'
    
    def handle(self, *args, **options):
        """
        Main command execution - creates all necessary MongoDB indexes
        """
        
        # Connect to MongoDB using environment variables
        client = pymongo.MongoClient(os.getenv('MONGODB_URI', 'mongodb://localhost:27017'))
        db = client[os.getenv('MONGODB_DB_NAME', 'myproject_db')]
        
        self.stdout.write('Initializing MongoDB indexes - November 29, 2025')
        
        # Create indexes for pages collection (if exists)
        self.stdout.write('Creating indexes for pages collection...')
        db.pages.create_index([("owner_id", 1), ("updated_at", -1)])  # User's recent pages
        db.pages.create_index([("url", 1)], unique=True)              # Unique URL constraint
        db.pages.create_index([("metadata.tags", 1)])                 # Tag-based searches
        
        # Create indexes for parcels collection - MAIN FOCUS
        self.stdout.write('Creating indexes for parcels collection...')
        
        # Most important: Fast tracking number lookups
        db.parcels.create_index([("tracking_number", 1)], unique=True)
        
        # Geographic queries for delivery optimization
        db.parcels.create_index([("recipient.address.zip", 1)])
        
        # Status and date-based queries for dashboard
        db.parcels.create_index([("current_status", 1), ("created_at", -1)])
        
        # Status history queries for tracking
        db.parcels.create_index([("status_history.timestamp", -1)])
        
        self.stdout.write(
            self.style.SUCCESS('Successfully created all database indexes')
        )
        self.stdout.write(
            self.style.SUCCESS('Database optimized for parcel tracking operations')
        )
        self.stdout.write(
            self.style.SUCCESS('Initialization completed on November 29, 2025')
        )
