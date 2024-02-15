from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from .forms import UserChangeForm, UserCreationForm
from .models import User


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = User
    list_display = (
        '__str__',
        'email',
        'first_name',
        'last_name',
        'get_groups',
        'is_staff',
        'is_superuser',
    )

    @admin.display(description='Grupos')
    def get_groups(self, obj):
        groups = obj.groups.all()
        if groups:
            return ', '.join([group.name for group in groups])