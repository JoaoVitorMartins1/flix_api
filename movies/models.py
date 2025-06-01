from django.db import models
from genres.models import Genre
from actors.models import Actor
# Create your models here.


class Movie(models.Model):
    title=models.CharField(max_length=500,null=False,blank=False)
    genre=models.ForeignKey(Genre, related_name='movies', on_delete=models.PROTECT)
    release_date=models.DateField(null=True,blank=True)
    actors=models.ManyToManyField(Actor,related_name='movies')
    resume=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.title