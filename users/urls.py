from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path, include
from users.apps import UsersConfig
from users.views import UserListView
from django.contrib import admin
from rest_framework_simplejwt.views import TokenRefreshView

from users.views import \
    LoginAPIView, \
    UserCreateAPIView, \
    UserRetrieveUpdateDestroyAPIView, \
    UserProfile

app_name = UsersConfig.name

urlpatterns = \
    [
        path('admin/', admin.site.urls),
        path('auth/', include('django.contrib.auth.urls')),
        path('logout/', LogoutView.as_view(), name='logout'),
        path('accounts/login/', LoginView.as_view(), name='login'),
        path('', UserListView.as_view(), name='users_list'),
    ] + \
    [
        path('api/token/',
             LoginAPIView.as_view(),
             name='token_obtain_pair'),

        path('api/registration/',
             UserCreateAPIView.as_view(),
             name='user_registration'),

        path('api/user/<int:pk>/',
             UserRetrieveUpdateDestroyAPIView.as_view(),
             name='user'),

        path('api/user/profile/<int:pk>/',
             UserProfile.as_view(),
             name='user_profile'),
    ]
