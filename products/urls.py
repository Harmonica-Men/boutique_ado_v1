from django.urls import path
from . import views
from .views import ProductDetailView

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>', ProductDetailView.as_view(), name='product_detail'),
]
