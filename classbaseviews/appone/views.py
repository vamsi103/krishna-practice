from django.shortcuts import render
from appone.models import Product
from django.views.generic import ListView,DetailView,CreateView


class ProductListView(ListView):
    model = Product

class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = ('ProductBrandName','ProductBrandModel','ProductBrandPrice')

# Create your views here.
