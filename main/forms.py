from django import forms
from main.models import Products

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'description', 'price', 'stock_quantity', 'detail', 'thumbnail', 'category', 
                  'product_group','is_featured', 'size', 'gender']