from rest_framework import serializers
from .models import Page, PageMetadata, PageAnalytics

class PageMetadataSerializer(serializers.Serializer):
    tags = serializers.ListField(child=serializers.CharField(), default=list)
    category = serializers.CharField(max_length=100, allow_blank=True, default='')
    author = serializers.CharField(max_length=255, allow_blank=True, default='')

class PageAnalyticsSerializer(serializers.Serializer):
    views = serializers.IntegerField(default=0)
    last_viewed = serializers.DateTimeField(allow_null=True, required=False)

class PageSerializer(serializers.ModelSerializer):
    metadata = PageMetadataSerializer(default=dict)
    analytics = PageAnalyticsSerializer(default=dict)
    
    class Meta:
        model = Page
        fields = ['_id', 'url', 'title', 'content', 'owner_id', 'created_at', 
                 'updated_at', 'status', 'metadata', 'analytics']
        read_only_fields = ['_id', 'created_at', 'updated_at']