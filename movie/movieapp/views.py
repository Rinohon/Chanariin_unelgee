from django.shortcuts import render
from rest_framework import generics
from .models import Movie, Genre
from .serializers import MovieAll, GenreAll

class MovieGetCreate(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieAll

class MovieUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieAll

class GenreGetCreate(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreAll

class GenreUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreAll