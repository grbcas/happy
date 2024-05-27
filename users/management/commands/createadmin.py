from django.core.management import BaseCommand

from users.models import User
import os


class Command(BaseCommand):
    """create admin user"""

    def handle(self, *args, **options):
        user, created = User.objects.get_or_create(
            email='super@user.ru',
            is_superuser=True,
            is_active=True,
            is_staff=True,
        )
        print(user, created)
        if created:
            user.set_password(os.getenv('ADMIN_PASSWORD'))
            user.save()
            return f'admin user: "{user.email}" was created {os.getenv("ADMIN_PASSWORD")}'
