from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView , ListView , DetailView , View
from .models import Category, Like, Product , Comments , Compare

class ProductsList(ListView):
    template_name = 'shop/shop.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 12
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class ProductDetail(DetailView):
    template_name = 'shop/shop-product.html'
    model = Product
    context_object_name = 'products'
    def get_context_data(self ,*args , **kwargs):
        context = super().get_context_data(*args , **kwargs)
        queryset = Product.objects.get(slug = self.object.slug)
        queryset.save()
        if self.request.user.is_authenticated == True:
            if self.request.user.likes.filter(products__english_title = self.object.english_title , users_id = self.request.user.id).exists():
                context['is_liked'] = True
            else:
                context['is_liked'] = False
        else:
            pass
        # if self.request.user.is_authenticated == True:
        #     if self.request.user.compares.filter(products__english_title = self.object.english_title , users_id = self.request.user.id).exists():
        #         context['is_compared'] = True
        #     else:
        #         context['is_compared'] = False
        # else:
        #     pass
        context['categories'] = Category.objects.all()
        return context
    def post(self , request , slug):
        products = Product.objects.get(slug=slug)
        parent_id = request.POST.get('parent_id')
        message = request.POST.get('message')
        Comments.objects.create(message=message, parent_id=parent_id , products=products , user=request.user)
        return redirect('shop:datail' , slug)

class CategoryDetails(View):
    queryset = None
    template_name = 'shop/shop.html'
    def get(self, request , pk):
        queryset = get_object_or_404(Category , id=pk)
        objects = queryset.products.all()
        category = Category.objects.all()
        return render (request , self.template_name , {'id':pk , 'products':objects , 'categories':category})

class LikeListView(TemplateView):
    template_name = 'shop/whish_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['likes'] = self.request.user.likes.all()
        return context

def like(request , slug , pk):
    try:
        like = Like.objects.get(products__slug = slug , users_id=request.user.id)
        like.delete()
    except:
        Like.objects.create(products_id=pk , users_id = request.user.id)
    return redirect('shop:likes_list')    

class LikeDeleteView(View):
    def get(self , request , slug):
        like = Like.objects.get(products__slug = slug , users_id=request.user.id)
        like.delete()
        return redirect('shop:likes_list')

# def compare(request , slug , pk):
#     try:
#         compare = Compare.objects.get(products__slug = slug , users_id=request.user.id)
#         compare.delete()
#     except:
#         Compare.objects.create(products_id=pk , users_id = request.user.id)
#     compare = Compare.objects.all()[:3]
#     return render(request , 'shop/compare.html' , {'compare':compare})

class CompareListView(TemplateView):
    template_name = 'shop/compare.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['compare'] = self.request.user.compares.all()[:3]
        return context
    
class Compares(View):
    template_name = 'shop/compare.html'
    def post(self , request , slug):
        product = get_object_or_404(Product , slug=slug)
        compare = request.user.compares.all()[:3]
        Compare.objects.create(products = product , users = request.user)
        return render(request , self.template_name , {'compare':compare})

class CompareDeleteView(View):
    def get(self , request , slug):
        compare = Compare.objects.get(products__slug = slug , users_id=request.user.id)
        compare.delete()
        return redirect('shop:compares_list')
    

