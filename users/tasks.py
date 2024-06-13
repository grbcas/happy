from config.celery import app
from users.models import User
from datetime import date
from users.services.mailing import notify


@app.task
def task_notify():
    """
    выбираем всех пользователей, которых сегодня ДР
    рассылаем всем друзьям выбранных пользователей напоминание
    """
    today = date.today()
    users_birthdays_today = User.objects.filter(
        birthday__month=today.month,
        birthday__day=today.day
    )
    print('users_birthdays_today>>>', users_birthdays_today)
    # for user in users_birthdays_today:
    #     friends = User.objects.values_list('friend', flat=True).filter(pk=user.pk)
    #     for friend in friends:
    #         if friend:
    #             friend_email = User.objects.values_list('email', flat=True).filter(pk=friend)
    #             notify.delay(user.email, friend_email[0])

    for user in users_birthdays_today:
        friends_emails = User.objects.values_list('email', flat=True).filter(friend__pk=user.pk)
        print('friends_emails>>>', friends_emails)
        for email in friends_emails:
            if email:
                print('user>>>', user, 'email>>>', email)
                # notify.delay(user, email)
                notify(user, email)
