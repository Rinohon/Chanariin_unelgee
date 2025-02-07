from django.db import models

class Genre(models.Model):
    genreId = models.AutoField(primary_key=True)
    genreName = models.CharField(max_length=50)

    def __str__(self):
        return self.genreName[:20]

class Movie(models.Model):
    kinoId = models.AutoField(primary_key=True)
    kinoNer = models.CharField(max_length=50)
    tailbar = models.CharField(max_length=200)
    release_date = models.DateField()
    image = models.ImageField(upload_to='movie_images/', null=True, blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.kinoNer[:20]
