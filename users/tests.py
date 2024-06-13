from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from users.services.mailing import notify
from users.models import User


class UserAPITestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            email='user@user.user',
            password='user@user.user',
        )

    def test_notify(self):
        """check response"""

        response = notify('user', 'user@user.user')

        self.assertEqual(response['ok'], True)
