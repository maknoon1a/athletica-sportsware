from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', show_main, name='main'),
    path('main/homepage/', show_products, name='homepage'),
    path('main/product/<str:id>/', product_detail, name='product_detail'),
    path('main/add-product/', add_product, name='add_product'),
    path('main/show-json/', show_json, name='show_data_json'),
    path('main/show-xml/', show_xml, name='show_data_xml'),
    path('main/show-json/<str:id>/', show_json_byID, name='show_data_json_byID'),
    path('main/show-xml/<str:id>/', show_xml_byID, name='show_data_xml_byID'),
    path('main/show-color/', show_color, name='show_color'),
    path('main/register/', user_register, name='register'),
    path('main/login/', user_login, name='login'),
    path('main/logout/', user_logout, name='logout'),
    path('main/user/cart/', user_cart, name='cart'),
    path('main/product/<str:id>/edit/', edit_product, name='edit_product'),
    path('main/product/<str:id>/delete/', delete_product, name='delete_product')
    # path('user/profile/', user_profile, name='profile')
]
