from django.contrib import admin
from users.models import User


# admin.site.register(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'email',
        'birthday',
        'is_active',
    )
    list_display_links = ('id', 'email')
    search_fields = ('email', 'birthday',)
