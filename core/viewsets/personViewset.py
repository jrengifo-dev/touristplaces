from rest_framework.viewsets import ModelViewSet
from core.models import Person
from core.serializers import PersonSerializer
from core.pagination import CustomPagination
from core.filters import PersonFilter
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class PersonViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_class = PersonFilter  
    search_fields = ['names','last_names','document_number']
    ordering_fields = ['id', 'document_number','created_at']
    ordering = ['id']