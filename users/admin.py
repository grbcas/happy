from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    list_display = (
        'id',
        'email',
        'birthday',
        'is_active',
        'display_friends',
    )

    list_display_links = ('id', 'email')
    search_fields = ('email', 'birthday',)
    ordering = ('email',)

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    # "first_name",
                    # "last_name",
                    "password1",
                    "password2",
                    "friend",
                    "birthday",
                ),
            },
        ),
    )
    fieldsets = (
        (None, {"fields": ("email", "password", "birthday")}),
        # ("Personal info", {"fields": ("first_name", "last_name")}),
        ("Friends", {"fields": ("friend", )}),
        # (
        #     "Permissions",
        #     {
        #         "fields": (
        #             "is_active",
        #             "is_staff",
        #             "is_superuser",
        #             "groups",
        #             "user_permissions",
        #         ),
        #     },
        # ),
        # ("Important dates", {"fields": ("last_login", "date_joined")}),
    )