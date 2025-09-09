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

    SIZE_CHOICES = [
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
        ('XXL', 'Double Extra Large'),
    ]
    
    GENDER_CHOICES = [
        ('men', 'Men'),
        ('women', 'Women'),
        ('unisex', 'Unisex'),
        ('kids', 'Kids'),
    ]

    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='jersey')
    is_featured = models.BooleanField(default=False)
    size = models.CharField(max_length=10, choices=SIZE_CHOICES, default='M')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='unisex')
    stock_quantity = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True)
    views_count = models.PositiveIntegerField(default=0)
