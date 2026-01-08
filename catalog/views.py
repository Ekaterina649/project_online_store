from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm
from catalog.models import Product
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect

class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'


class ProductDetailView(LoginRequiredMixin,DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class ContactsView(LoginRequiredMixin,TemplateView):
    template_name = 'catalog/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['success'] = self.request.GET.get('success') == '1'
        if context['success']:
            context['name'] = self.request.GET.get('name')
            context['phone'] = self.request.GET.get('phone')
            context['message'] = self.request.GET.get('message')
        return context

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        url = reverse('catalog:contacts')
        return redirect(f"{url}?success=1&name={name}&phone={phone}&message={message}")


class ProductCreateView(LoginRequiredMixin,CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_post_form.html'
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(LoginRequiredMixin,UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_post_form.html'

    def get_success_url(self):
        return reverse('catalog:product_detail', kwargs={'pk': self.object.pk})

class ProductDeleteView(LoginRequiredMixin,DeleteView):
    model = Product
    template_name = 'catalog/post_confirm_delete.html'
    success_url = reverse_lazy('catalog:product_list')
