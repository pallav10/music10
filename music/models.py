from __future__ import unicode_literals
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.


class Genre(models.Model):
    class Meta:
        db_table = 'genre'
    genre = models.CharField(max_length=100)
    is_favorite = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.genre


class Song(models.Model):
    class Meta:
        db_table = 'song'

    song_title = models.CharField(max_length=250)
    genre = models.CharField(max_length=100)
    audio_file = models.FileField(default='')
    ratings = models.IntegerField(default=0,
                                  validators=[MaxValueValidator(5), MinValueValidator(0)])
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title
