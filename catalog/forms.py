from django import forms
from django.core.exceptions import ValidationError

from catalog.models import Product

FORBIDDEN_WORDS = [
    'казино',
'криптовалюта',
'крипта',
'биржа',
'дешево',
'бесплатно',
'обман',
'полиция',
'радар',
]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product

        fields = '__all__'
        exclude = ['created_at','updated_at']

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
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите название продукта'})
        self.fields['description'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Введите описание продукта'})
        self.fields['image'].widget.attrs.update({'class': 'form-control'})
        self.fields['category'].widget.attrs.update({'class': 'form-control'})
        self.fields['price'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите цену продукта'})



