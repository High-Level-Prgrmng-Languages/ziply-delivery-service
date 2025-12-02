import uuid
from django.db import models
from djongo import models as djongo_models


def generate_uuid():
    return str(uuid.uuid4())


class PageMetadata(djongo_models.Model):
    tags = models.JSONField(default=list)
    category = models.CharField(max_length=100, blank=True)
    author = models.CharField(max_length=255, blank=True)

    class Meta:
        abstract = True


class PageAnalytics(djongo_models.Model):
    views = models.IntegerField(default=0)
    last_viewed = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True


class Page(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('archived', 'Archived'),
    ]

    _id = models.CharField(
        max_length=36, primary_key=True, default=generate_uuid)
    url = models.URLField(unique=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    owner_id = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='active')
    metadata = djongo_models.EmbeddedModelField(
        model_container=PageMetadata, default=dict)
    analytics = djongo_models.EmbeddedModelField(
        model_container=PageAnalytics, default=dict)

    class Meta:
        db_table = 'pages'
        ordering = ['-updated_at']
