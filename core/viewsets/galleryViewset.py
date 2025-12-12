from rest_framework.viewsets import ModelViewSet
from core.models import Gallery
from core.serializers import GallerySerializer

class GalleryViewSet(ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer