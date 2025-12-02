from django.urls import path
from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
)

app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='post_list'),
    path('create/', BlogCreateView.as_view(), name='post_create'),
    path('detail/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('edit/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('delete/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
]