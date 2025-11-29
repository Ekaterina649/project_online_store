from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Очищает базу и загружает данные из фикстур Category и Product"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING("Удаляем старые данные..."))

        Product.objects.all().delete()
        Category.objects.all().delete()

        self.stdout.write(self.style.SUCCESS("Старые данные удалены."))

        self.stdout.write(self.style.WARNING("Загружаем фикстуры..."))

        # Используем существующие фикстуры
        try:
            call_command("loaddata", r"catalog/fixtures/categories.json")
            call_command("loaddata", "catalog/fixtures/products.json")
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Ошибка при загрузке фикстур: {e}"))
            return

        self.stdout.write(self.style.SUCCESS("Фикстуры успешно загружены!"))

        # Проверка связей
        self.stdout.write("Проверяем связи продуктов и категорий:")
        for product in Product.objects.all():
            self.stdout.write(f" → {product.name} — категория: {product.category.name}")

        self.stdout.write(self.style.SUCCESS("Загрузка завершена успешно!"))
