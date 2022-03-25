from django.contrib import admin

from chat.models import Msg


@admin.register(Msg)
class PersonAdmin(admin.ModelAdmin):
    pass
