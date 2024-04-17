from django.contrib import admin

from menu.models import Categories, Dishs

# admin.site.register(Categories)
# admin.site.register(Dishs)

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Dishs)
class DishsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}