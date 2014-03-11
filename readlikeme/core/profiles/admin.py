from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from readlikeme.core.profiles.models import Reader
from django.contrib.auth.forms import UserChangeForm
from readlikeme.core.profiles.forms import ReaderChangeForm

class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Reader

class ReaderAdmin(UserAdmin):
    form = ReaderChangeForm

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('bio', 'followers',)}),
    )


admin.site.register(Reader, ReaderAdmin)
