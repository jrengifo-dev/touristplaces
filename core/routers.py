from rest_framework.routers import DefaultRouter
from core.viewsets import *

router = DefaultRouter()

router.register(r'persons', PersonViewSet, basename='person')
router.register(r'places', PlaceViewSet, basename='place')
router.register(r'galleries', GalleryViewSet, basename='gallery')
router.register(r'reviews', ReviewViewSet, basename='review')
router.register(r'ubigeos', UbigeoViewSet, basename='ubigeos')