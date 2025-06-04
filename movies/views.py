from django.db.models import Count, Avg
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .permissions import MoviePermissionsClass
from .serializers import MoviesSerializer, MovieListDetailSerializer
from .models import Movie
from reviews.models import Review


class MoviesCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, MoviePermissionsClass,)
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListDetailSerializer
        return MoviesSerializer


class MoviesRetrieveUpdateView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, MoviePermissionsClass,)
    queryset = Movie.objects.all()


    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListDetailSerializer
        return MoviesSerializer


class MovieStatsView(APIView):
    permission_classes = (IsAuthenticated, MoviePermissionsClass,)
    queryset = Movie.objects.all()

    def get(self, request):
        total_movies = Movie.objects.all().count()
        movies_by_genere = Movie.objects.all().values('genre__name').annotate(count=Count('id'))
        total_reviews = Review.objects.count()
        average_stars = Review.objects.aggregate(Avg('stars'))['stars__avg']
        return Response(
            data={
                "total_movies": total_movies,
                "movies_by_genere": movies_by_genere,
                "total_reviews": total_reviews,
                "averege_stars":round(average_stars,2)
            }
        )
