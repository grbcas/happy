from django.core.management import BaseCommand
from users.services.mailing import notify


class Command(BaseCommand):
    """
    Команда - отправить письма клиентам
    """

    def handle(self, *args, **options) -> None:
        notify('grbcas@yandex.ru', 'grbcas@yandex.ru')

