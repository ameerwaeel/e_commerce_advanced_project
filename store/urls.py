from . import views
from django.urls import path
app_name='store'
urlpatterns = [
    path('',views.list_products,name="home"),
    path('category/<slug:slug>/',views.list_products,name="category_detail"),

    path('product/<slug:product_slug>/',views.products_detail,name="products_detail"),

    path('search/',views.product_search,name="product_search"),


]
