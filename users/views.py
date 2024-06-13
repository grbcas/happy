from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.views import TokenObtainPairView

from django.views.generic import ListView
from users.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from users.serializers import UserSerializer
from users.permissions import IsOwner, IsProfileOwner


class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'users/users_list.html'
    ordering = 'email'


class UserCreateAPIView(CreateAPIView):
    """New user creation"""

    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        """Set password as hash """

        # user = super().perform_create(serializer)
        user = serializer.save()

        if user is not None:
            password = self.request.data['password']
            user.set_password(password)
            user.save()
        return user


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):

    serializer_class = UserSerializer
    permission_classes = [IsOwner]
    queryset = User.objects.all()


class UserProfile(ListAPIView):
    permission_classes = [IsProfileOwner]
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        print(f"{request = }")
        print(f"{args = }")
        print(f"{kwargs = }")
        pk = self.kwargs.get("pk")
        friends_emails = User.objects.values_list('email', flat=True).filter(friend__pk=pk)
        print(friends_emails)
        data = {'friends_emails': ', '.join(friends_emails)}
        print(data)
        return Response(data=friends_emails, status=200)


class LoginView(TokenObtainPairView):
    """Authentication via token"""
    def post(self, request: Request, *args, **kwargs) -> Response:
        """add private key at the first login"""
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
            email = request.data.get('email')
            user = User.objects.get(email=email)
            user.add_own_invite_key()
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)