from django import forms
from main.models import Products

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'price', 'stock_quantity', 'colors', 'description', 'thumbnail', 'category', 
                  'product_group','is_featured', 'size', 'gender']
        widgets = {
            'colors': forms.CheckboxSelectMultiple,
        }