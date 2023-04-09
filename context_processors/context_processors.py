from account.models import User
from shop.models import Category, Product
from django.core.paginator import Paginator
from cart.cart_module import Cart


def context_for_site(request):
    category = Category.objects.all() 
    products = Product.objects.all()
    slider = Product.objects.all()[:7]
    slider2 = Product.objects.all()[:3]
    cart = Cart(request)
    return {"categories": category , 'products':products , 'sliders':slider , 'cart':cart , 'sliders2' : slider2}
