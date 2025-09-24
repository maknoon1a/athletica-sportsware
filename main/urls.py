from django.urls import path
from main.views import show_main, show_json, show_xml, show_xml_byID, show_json_byID, add_product, show_color, show_products, product_detail, user_register, user_login, user_logout, user_cart

app_name = 'main'

urlpatterns = [
    path('', show_main, name='main'),
    path('homepage/', show_products, name='homepage'),
    path('product/<str:id>/', product_detail, name='product_detail'),
    path('add-product/', add_product, name='add_product'),
    path('show-json/', show_json, name='show_data_json'),
    path('show-xml/', show_xml, name='show_data_xml'),
    path('show-json/<str:id>/', show_json_byID, name='show_data_json_byID'),
    path('show-xml/<str:id>/', show_xml_byID, name='show_data_xml_byID'),
    path('show-color/', show_color, name='show_color'),
    path('register/', user_register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('user/cart', user_cart, name='cart'),
    # path('user/profile/', user_profile, name='profile')
]
