from django.urls import path
from main.views import show_main, show_json, show_xml, show_xml_byID, show_json_byID, add_product, show_color, show_products, product_detail

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('main/products', show_products, name='products'),
    path('main/products/<str:id>', product_detail, name='product_detail'),
    path('main/add-product', add_product, name='add_product'),
    path('main/show-json', show_json, name='show_data_json'),
    path('main/show-xml', show_xml, name='show_data_xml'),
    path('main/show-json/<str:id>', show_json_byID, name='show_data_json_byID'),
    path('main/show-xml/<str:id>', show_xml_byID, name='show_data_xml_byID'),
    path('main/show-color', show_color, name='show_color')
]
