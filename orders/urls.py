from django.urls import path
from .views import CartDetailView, AddToCartView, RemoveFromCartView, checkout, OrderHistoryView

urlpatterns = [
    path('cart/', CartDetailView.as_view(), name='cart_detail'),
    path('add_to_cart/<int:pk>/', AddToCartView.as_view(), name='add_to_cart'),
    path('remove_from_cart/<int:pk>/', RemoveFromCartView.as_view(), name='remove_from_cart'),
    path('checkout/', checkout, name='checkout'),
    path('order_history/', OrderHistoryView.as_view(), name='order_history'),
]
