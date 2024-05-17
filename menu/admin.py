from django.contrib import admin

from menu.models import Categories, Dishs

# admin.site.register(Categories)
# admin.site.register(Dishs)

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name']

@admin.register(Dishs)
class DishsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'price', 'discount']
    list_editable = ['discount',]
    search_fields = ['name', 'description']
    list_filter = ['discount', 'category']
    fields = [
        "name",
        "category",
        "slug",
        "description",
        "image",
        ("price", "discount")
    ]