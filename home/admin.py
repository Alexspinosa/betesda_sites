from django.contrib import admin
from menu.models import Menu, MenuItem   #  Importar desde la app menu

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    search_fields = ('title',)

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'menu', 'link_url', 'link_page', 'open_in_new_tab')
    list_filter = ('menu',)
    search_fields = ('title',)
