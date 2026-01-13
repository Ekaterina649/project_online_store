from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):

    def handle(self, *args, **options):
        group, created = Group.objects.get_or_create(
            name='Модератор продуктов'
        )

        permissions = Permission.objects.filter(
            codename__in=[
                'delete_product',
                'can_unpublish_product',
            ]
        )

        group.permissions.set(permissions)

        if created:
            self.stdout.write(self.style.SUCCESS(
                'Группа "Модератор продуктов" создана'
            ))
        else:
            self.stdout.write(self.style.WARNING(
                'Группа "Модератор продуктов" уже существует'
            ))