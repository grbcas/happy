from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from users.services.telegram import telegram_bot_message
from users.models import User


class UserAPITestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            email='user@user.user',
            password='test_user',
        )

    def test_telegram_bot_message(self):
        """check telegram request response"""

        response = telegram_bot_message('test_message', '559773959')

        # response = {'ok': True,
        #             'result': {'message_id': 140, 'from': {'id': 6542037151, 'is_bot': True, 'first_name': 'skybot_27',
        #                                                    'username': 'skybot27_bot'},
        #             'chat': {'id': 559773959, 'first_name': 'Alexander', 'username': 'grbcas',
        #             'type': 'private'}, 'date': 1701194543,
        #             'text': 'test'}}

        # assert response['ok'] is True

        self.assertEqual(response['ok'], True)
