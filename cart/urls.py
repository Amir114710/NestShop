from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('' , views.CartDetailView.as_view() , name='cart_main'),
    path('add/<slug:slug>' , views.CartAddView.as_view() , name='cart_add'),
    path('delete/<str:id>' , views.CartDeleteView.as_view() , name='cart_delete'),
    path('order_detail/<int:pk>' , views.OrderDetailView.as_view() , name='order_detail'),
    path('order_add' , views.OrderCreationView.as_view() , name='order_add'),
    path('apply_discount/<int:pk>' , views.ApplyDiscountView.as_view() , name='apply_discount'),
    path('apply_address/<int:pk>' , views.ApplyAddress.as_view() , name='apply_address'),
]