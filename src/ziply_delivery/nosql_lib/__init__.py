"""
NoSQL Library - A Python library for MongoDB operations
"""

from .client import NoSQLClient
from .models import Document, EmbeddedDocument
from .fields import StringField, IntegerField, DateTimeField, ArrayField
from .query import QueryBuilder

__version__ = "1.0.0"
__all__ = ['NoSQLClient', 'Document', 'EmbeddedDocument', 'QueryBuilder']