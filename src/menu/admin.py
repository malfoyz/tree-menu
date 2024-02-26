from django.contrib import admin

from .models import Menu, MenuItem


class MenuItemAdmin(admin.ModelAdmin):
    """Редактор модели MenuItem."""

    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Menu)
admin.site.register(MenuItem, MenuItemAdmin)
