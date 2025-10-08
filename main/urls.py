from django.conf import settings
from django.urls import path
from main.views import *
from django.conf.urls.static import static

app_name = 'main'

urlpatterns = [
    path('', show_main, name='main'),
    path('main/homepage/', show_homepage, name='homepage'),
    path('main/mainpage/', show_products, name='products'),
    path('main/product/<str:id>/', product_detail, name='product_detail'),
    path('main/add-product/', add_product, name='add_product'),
    path('main/show-json/', show_json, name='show_data_json'),
    path('main/show-xml/', show_xml, name='show_data_xml'),
    path('main/show-json/<str:id>/', show_json_byID, name='show_data_json_byID'),
    path('main/show-xml/<str:id>/', show_xml_byID, name='show_data_xml_byID'),
    path('main/register/', user_register, name='register'),
    path('main/login/', user_login, name='login'),
    path('main/logout/', user_logout, name='logout'),
    path('main/user/cart/', user_cart, name='cart'),
    path('main/product/<str:id>/edit/', edit_product, name='edit_product'),
    path('main/product/<str:id>/delete/', delete_product, name='delete_product'),
    
    # AJAX endpoints
    path('main/ajax/add-product/', add_product_ajax, name='add_product_ajax'),
    path('main/ajax/update-product/<str:id>/', update_product_ajax, name='update_product_ajax'),
    path('main/ajax/delete-product/<str:id>/', delete_product_ajax, name='delete_product_ajax'),
    path('main/ajax/products-partial/', products_partial, name='products_partial'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)