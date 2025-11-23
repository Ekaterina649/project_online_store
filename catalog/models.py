from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, verbose_name="Описание", default='', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'



class Product(models.Model):
    name = models.CharField(max_length=100,verbose_name='Название продукта')
    description = models.CharField(max_length=200,verbose_name="Описание",default='',null=True,blank=True)
    image = models.ImageField(upload_to='photos',verbose_name='Фото',null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,verbose_name='категория',blank=True, null=True)
    price = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='цена за покупку')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} {self.category} {self.price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


