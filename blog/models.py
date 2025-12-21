from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='blog/previews/', verbose_name='Превью', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')
    views_count = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')


    class Meta:
        verbose_name = "публикация"
        verbose_name_plural = "публикации"
        ordering = ['-created_at']

    def __str__(self):
        return self.title
