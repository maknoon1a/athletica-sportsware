from django.db import models

# Create your models here.
class Product(models.Model):

    CATEGORY_CHOICES = [
        ('jersey', 'Jersey'),
        ('shorts', 'Shorts'),
        ('shoes', 'Shoes'),
        ('tracksuit', 'Tracksuit'),
        ('accessories', 'Accessories'),
        ('equipment', 'Equipment'),
    ]

    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='jersey')
    is_featured = models.BooleanField(default=False)
