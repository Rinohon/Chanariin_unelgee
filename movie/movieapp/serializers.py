from rest_framework import serializers
from movieapp.models import Movie, Genre

class MovieAll(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class GenreAll(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'