from rest_framework import generics
from movies.models import Movie
from movies.serializers import MoviesSerializer


class MovieCreateListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MoviesSerializer


class MovieRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MoviesSerializer


