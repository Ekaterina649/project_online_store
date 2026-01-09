from django.urls import path
from .views import ProductListView, ContactsView, ProductDetailView, ProductCreateView, ProductDeleteView, \
    ProductUpdateView, ProductUnpublishView

app_name = 'catalog'

urlpatterns = [path('',ProductListView.as_view(),name='product_list'),
               path('contacts/',ContactsView.as_view(), name='contacts'),
               path('product_detail/<int:pk>/',ProductDetailView.as_view(), name='product_detail'),
               path('create/',ProductCreateView.as_view(), name='post_create'),
               path('delete/<int:pk>/',ProductDeleteView.as_view(), name='product_delete'),
               path('update/<int:pk>/',ProductUpdateView.as_view(), name='product_edit'),
               path('unpublish/<int:pk>/', ProductUnpublishView.as_view(), name='product_unpublish'),
               ]

