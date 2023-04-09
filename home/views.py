from django.shortcuts import render
from django.views.generic import TemplateView

from shop.models import Category, Product


class HomeView(TemplateView):
    template_name = 'home/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['products'] = Product.objects.all()
        return context
