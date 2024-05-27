from celery import shared_task


@shared_task
def mailing(uid, email):
    print(f'notify {email} >>> {uid} celebrates birthday today')
