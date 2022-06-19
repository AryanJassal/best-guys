from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
from apps.core.models import User


class Product(models.Model):
    name = models.CharField(max_length=255)
    long_name = models.CharField(max_length=511)
    slug = models.SlugField(max_length=255, unique=True)
    model = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, default=-1.0)
    image_url = models.URLField()
    reviews = models.ManyToManyField('Review', blank=True)
    specifications = models.ManyToManyField('Specification', blank=True)

    def __str__(self):
        return self.name
    
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    recommended = models.BooleanField(default=False)
    star_rating = models.PositiveIntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.name

class Specification(models.Model):
    label = models.CharField(max_length=255)
    specification = models.CharField(max_length=255)

    def __str__(self):
        return self.label
