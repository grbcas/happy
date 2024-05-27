from celery import shared_task

from config.celery import app
from users.models import User
from datetime import date
from users.services.mailing import mailing


@app.task
def task_notify():
    """
    выбираем всех пользователей, которых сегодня ДР
    рассылаем всем друзьям выбранных пользователей напоминание
    :param:
    :return:
    """
    today = date.today()
    print('today>>>>', today)
    users_birthdays_today = User.objects.filter(
        birthday__month=today.month,
        birthday__day=today.day
    )
    print(users_birthdays_today)

    for user in users_birthdays_today:
        friends = User.objects.values_list('friend', flat=True).filter(pk=user.pk)
        print(friends)
        for friend in friends:
            print('friend>>>', friend)
            if friend:
                friend_email = User.objects.values_list('email', flat=True).filter(pk=friend)
                mailing.delay(user.name, friend_email)
