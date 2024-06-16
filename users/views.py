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


class LoginAPIView(TokenObtainPairView):
    """Authentication with token"""
    def post(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):

    serializer_class = UserSerializer
    permission_classes = [IsOwner]
    queryset = User.objects.all()

    def patch(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )


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
