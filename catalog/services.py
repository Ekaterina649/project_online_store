from django.core.cache import cache

from catalog.models import Product
from config import settings


class ProductService:

    @staticmethod
    def get_product_by_category(category_id):
        if getattr(settings, 'CACHE_ENABLED', False):
            cache_key = f'products_category_{category_id}'
            products = cache.get(cache_key)
            if products is None:
                products = list(Product.objects.filter(category_id=category_id))
                cache.set(cache_key, products, 60 * 15)
            return products
        else:
            return Product.objects.filter(category_id=category_id)
