
from shop.models import Product


CART_SESSION_ID = 'cart'

class Cart:
    def __init__(self , request):
        self.session = request.session
        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}
        self.cart = cart
    
    def __iter__(self):
        cart = self.cart.copy()
        for item in cart.values():
            product = Product.objects.get(id = int(item['id']))
            item['product'] = product
            item['total'] = int(item['quantity']) * int(item['price'])
            item['unique_id'] = self.id_generator(product.id , item['size'])
            yield item

    def remove_cart(self):
        del self.session[CART_SESSION_ID]
        self.save()

    def id_generator(self , id , size):
        result = f'{id}--{size}'
        return result
    
    def add(self, product, quantity , size):
        unique = self.id_generator(product.id , size)
        if unique not in self.cart:
            self.cart[unique] = {'quantity': 0 , 'price': str(product.price) , 'size':size , 'id' : product.id}
        self.cart[unique]['quantity'] += int(quantity)
        self.save()

    def total(self):
        cart = self.cart.values()
        total = sum(int(item['price']) * int(item['quantity']) for item in cart)
        return total

    def delete(self , id):
        if id in self.cart:
            del self.cart[id]
            self.save()

    def save(self):
        self.session.modified = True