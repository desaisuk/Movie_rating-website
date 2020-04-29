from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Movie(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()

    def __str__(self):
        return self.title


class MovieReview(models.Model):
    title = models.CharField(max_length=100, null=True)
    rating  = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)], default=1)
    comment  = models.TextField()

    def __str__(self):
        return self.title

