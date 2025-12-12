from rest_framework.viewsets import ModelViewSet
from core.models import Place
from core.serializers import PlaceSerializer
from core.pagination import CustomPagination
from rest_framework import filters

class PlaceViewSet(ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.OrderingFilter,filters.SearchFilter]
    search_fields = ['name','ubigeo__district']
    ordering_fields = ['id', 'created_at', 'ubigeo__region', 'ubigeo__province', 'ubigeo__district']
    ordering = ['id']