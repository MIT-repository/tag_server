from django.db import models

# Create your models here.

class Song(models.Model):
    bucket = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    genre = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    def get_genre(self):
        return self.genre
