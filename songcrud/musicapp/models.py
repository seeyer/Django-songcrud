from datetime import date
import datetime
from operator import mod
from unittest.util import _MAX_LENGTH
from django.db import models

from songcrud.songcrud.settings import DATABASES

# Create your models here.

class Artise(models.Model):
    First_name = models.CharField(_MAX_LENGTH=400)
    Last_name = models.CharField(_MAX_LENGTH=400)
    Age= models.IntegerField(_MAX_LENGTH=3)

class Song(models.Model):
    Title = models.CharField(_MAX_LENGTH=400)
    Date = models.DateTimeField(datetime)
    Likes = models.IntegerField(_MAX_LENGTH=5)
    Artise_id = models.IntegerField(_MAX_LENGTH=10)

class Lyric(models.Model):
    content =models.CharField(_MAX_LENGTH=1000)
    Song_id =models.IntegerField(_MAX_LENGTH=10)
