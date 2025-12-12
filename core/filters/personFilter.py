from django_filters import rest_framework as filters
from core.models import Person

class PersonFilter(filters.FilterSet):
    class Meta:
        model = Person
        fields = {
            'id': ['exact'],
            'names': ['icontains'],
            'last_names': ['icontains'],
            'document_number': ['exact', 'icontains'],
            'created_at': ['gte', 'lte'],

        }