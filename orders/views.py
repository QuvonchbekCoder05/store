from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.core.mail import send_mail
from .models import Order, OrderItem
from products.models import Product

class CartDetailView(LoginRequiredMixin, View):
    def get(self, request):
        order = Order.objects.filter(user=request.user, is_completed=False).first()
        return render(request, 'orders/cart_detail.html', {'order': order})

class AddToCartView(LoginRequiredMixin, View):
    def post(self, request, pk):
        product = Product.objects.get(pk=pk)
        selected_color = request.POST.get('color')
        quantity = request.POST.get('quantity', 1)
        order, created = Order.objects.get_or_create(user=request.user, is_completed=False)
        order_item, created = OrderItem.objects.get_or_create(order=order, product=product, selected_color=selected_color)
        order_item.quantity += int(quantity)
        order_item.save()
        return redirect('cart_detail')

class RemoveFromCartView(LoginRequiredMixin, View):
    def post(self, request, pk):
        order_item = OrderItem.objects.get(pk=pk)
        order_item.delete()
        return redirect('cart_detail')

def checkout(request):
    order = Order.objects.get(user=request.user, is_completed=False)
    order.is_completed = True
    order.save()
    
    user_email = request.user.email
    store_owner_email = 'quvonchbek5045@gmail.com'
    
    # Send email to store owner and user
    send_mail(
        'New Order',
        f'User {request.user.username} has placed an order.',
        'shobirov198@gmail.com',
        [store_owner_email, user_email],
        fail_silently=False,
    )
    return redirect('product_list')

class OrderHistoryView(LoginRequiredMixin, View):
    def get(self, request):
        orders = Order.objects.filter(user=request.user, is_completed=True).order_by('-created_at')
        return render(request, 'orders/order_history.html', {'orders': orders})
