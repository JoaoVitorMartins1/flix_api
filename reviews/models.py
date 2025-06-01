from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from movies.models import Movie


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name="reviews")
    stars = models.IntegerField(
        validators=[
            MinValueValidator(0, "Essa avaliação deve ser maior que 0"),
            MaxValueValidator(5, "A avaliação nao pode ser superior a 5 estrelas"),
        ],
        null=False,
        blank=False,
    )
    comment = models.TextField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.movie
