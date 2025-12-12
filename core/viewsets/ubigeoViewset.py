from rest_framework.viewsets import ModelViewSet
from core.models import Ubigeo  
from core.serializers import UbigeoSerializer
from rest_framework import filters

class UbigeoViewSet(ModelViewSet):
    queryset = Ubigeo.objects.all()
    serializer_class = UbigeoSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['region', 'province', 'district','code']
    ordering_fields = ['id', 'region', 'province', 'district','code']
    ordering = ['id']
