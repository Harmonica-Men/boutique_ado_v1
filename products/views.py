
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from .models import Product
from django.shortcuts import render, get_object_or_404


# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


class ProductDetailView(DetailView):
    """ A class-based view to show individual product details """
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'

    def get_object(self):
        product_id = self.kwargs.get("product_id")
        return get_object_or_404(Product, pk=product_id)

