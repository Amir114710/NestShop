from django.shortcuts import render , redirect , get_object_or_404
from django.views.generic import View , TemplateView
from django.urls import reverse
from account.models import Address
from cart.cart_module import Cart
from shop.models import  Product
from .cart_module import Cart
from .models import DiscountCode, Order, OrderItem
from mixins import AddressRequirdMixins, LoginRequirdMixins , LogoutRequirdMixins

class CartDetailView(TemplateView):
    template_name = 'cart/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = Cart(self.request)
        return context

class CartAddView(View):
    def post(self , request , slug):
        product = get_object_or_404(Product , slug = slug)
        quantity = request.POST.get('quantity')
        size = request.POST.get('size')
        print(size , quantity)
        cart = Cart(request)
        cart.add(product , quantity , size)
        return redirect(reverse('cart:cart_main'))
    
class CartDeleteView(View):
    def get(self , request , id):
        print(id)
        cart = Cart(request)
        cart.delete(id)
        return redirect(reverse('cart:cart_main'))
    
class OrderDetailView(AddressRequirdMixins , View):
    def get(self , request , pk):
        order = get_object_or_404(Order , id=pk)
        return render(request , 'cart/checkout.html' , {'order':order})

class OrderCreationView(AddressRequirdMixins , View):
    def get(self , request):
        cart = Cart(request)
        order = Order.objects.create(user = request.user , total_price = cart.total())
        for item in cart:
            OrderItem.objects.create(order=order , product = item['product'] , quantity = item['quantity'] , price = item['price'])
        cart.remove_cart()
        return redirect('cart:order_detail' , order.id)
    
class ApplyDiscountView(AddressRequirdMixins , View):
    def post(self , request , pk):
        code = request.POST.get('discount_code')
        order = get_object_or_404(Order , id=pk)
        discount_code = get_object_or_404(DiscountCode , name=code)
        if discount_code.quantity == 0 :
            return redirect('cart:order_detail' , order.id)
        order.total_price -= order.total_price * discount_code.discount/100
        order.save()
        discount_code.quantity -= 1
        discount_code.save()
        return redirect('cart:order_detail' , order.id)

class ApplyAddress(AddressRequirdMixins , View):
    def post(self , request , pk):
        order = get_object_or_404(Order , id=pk)
        address = request.POST.get('address')
        order.addresses = address
        order.save()
        return redirect('home:main')