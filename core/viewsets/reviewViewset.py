from rest_framework.viewsets import ModelViewSet
from core.models import Review
from core.serializers import ReviewSerializer
from core.pagination import CustomPagination
from rest_framework import filters

class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['rating', 'created_at']
    ordering = ['-created_at']