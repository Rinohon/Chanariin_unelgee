from django.db import models

# Create your models here.
class Movie(models.Model):
    kinoNer = models.CharField(max_length=50)
    tailbar = models.CharField(max_length=200)
    release_date = models.DateField()

    def __str__(self):
        return self.kinoNer[:20]
    
    