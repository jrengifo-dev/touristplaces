from rest_framework import serializers
from core.models import Gallery

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'