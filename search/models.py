from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.


class Ad(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100000000)])
    image = models.ImageField(upload_to='ad/%Y/%m/%d/')
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
