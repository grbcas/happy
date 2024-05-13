from celery import shared_task


@shared_task
def task_send_code(code):
    print('user.verification_code', code)