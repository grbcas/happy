from celery import shared_task


@shared_task
def mailing(name, email):
    print(f'notify {email} >>> {name} celebrates birthday today')
