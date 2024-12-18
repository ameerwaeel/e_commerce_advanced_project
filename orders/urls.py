from . import views
from django.urls import path
app_name='orders'
urlpatterns = [
    path('create/',views.order_create,name="order_create"),
    path('pay_order/<int:order_id>/', views.order_pay_by_vodafon, name="order_pay_by_vodafon"),
    path('payment_success/<int:order_id>/', views.payment_success, name="payment_success"),
    # path('admin/pdf/<int:order_id>/', views.admin_order_id, name="admin_order_id"),


]

