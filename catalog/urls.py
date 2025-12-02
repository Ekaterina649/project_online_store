from django.urls import path
from . import views


app_name = 'catalog'

urlpatterns = [path('',views.index,name='home'),
               path('contacts/',views.contacts, name='contacts'),
               path('product_detail/<int:pk>/',views.product_detail, name='product_detail'),]

