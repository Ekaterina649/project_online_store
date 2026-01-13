from django import forms
from django.core.exceptions import ValidationError

from catalog.models import Product
from catalog.templates.catalog.constants import FORBIDDEN_WORDS


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product

        fields = '__all__'
        exclude = ['created_at','updated_at',]

    def clean_name(self):
            name = self.cleaned_data.get('name')
            for word in FORBIDDEN_WORDS:
                if word.lower() in name.lower():
                    raise ValidationError("Данное слово включено в список запрещенных слов")
            return name

    def clean_description(self):
            description = self.cleaned_data.get('description')
            for word in FORBIDDEN_WORDS:
                if word.lower() in description.lower():
                    raise ValidationError("Данное слово включено в список запрещенных слов")
            return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError("Цена не может быть отрицательной")
        return price

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            self.fields['owner'].initial = user
            self.fields['owner'].disabled = True

        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['image'].widget.attrs.update({'class': 'form-control'})
        self.fields['category'].widget.attrs.update({'class': 'form-control'})
        self.fields['price'].widget.attrs.update({'class': 'form-control'})

        if not user or not user.has_perm('catalog.can_unpublish_product'):
            self.fields.pop('is_published')
