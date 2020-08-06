from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, Rubric



class ProductView(ListView):
    """Список товаров"""
    model = Product
    context_object_name = "products"
    template_name = "intstore/index.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['products'] = Product.objects.all()
        context['rubrics'] = Rubric.objects.all()
        return context


class ProductDetailView(DetailView):
    """Полное описание товара"""
    model = Product
    id = "id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context
