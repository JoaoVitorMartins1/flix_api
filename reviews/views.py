from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permissions import ReviewPermissionsClass
from .models import Review
from.serializers import ReviewSerializer

class ReviewListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,ReviewPermissionsClass,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,ReviewPermissionsClass,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer