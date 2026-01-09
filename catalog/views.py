from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm
from catalog.models import Product
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect, get_object_or_404


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

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # передаём user в форму
        return kwargs

    def form_valid(self, form):
        form.instance.owner = self.request.user  # автоматически ставим текущего пользователя
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_post_form.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if not (
            request.user.is_superuser or
            obj.owner == request.user or
            request.user.groups.filter(name='Модератор продуктов').exists()
        ):
            return redirect('catalog:product_list')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('catalog:product_detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/post_confirm_delete.html'
    success_url = reverse_lazy('catalog:product_list')
    permission_required = 'catalog.delete_product'

    def has_permission(self):
        # Суперпользователь всегда может
        if self.request.user.is_superuser:
            return True

        # Проверка базового разрешения
        if not super().has_permission():
            return False

        product = self.get_object()
        # Владелец или модератор
        return (
            product.owner == self.request.user or
            self.request.user.groups.filter(name='Модератор продуктов').exists()
        )






class ProductUnpublishView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'catalog.can_unpublish_product'

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.is_published = False
        product.save()
        return redirect('catalog:product_detail', pk=pk)
