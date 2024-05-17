from django.contrib import admin

from carts.models import Cart


class CartTabAdmin(admin.TabularInline):
    model = Cart
    fields = 'dish', 'quantity', 'created_timestamp'
    search_fields = 'dish', 'quantity', 'created_timestamp'
    readonly_fields = ('created_timestamp',)
    extra = 1


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user_display', 'dish', 'quantity', 'created_timestamp',]
    list_filter = ['created_timestamp', 'user', 'dish__name',]

    def user_display(self, obj):
        if obj.user:
            return str(obj.user)
        return "Анонімний користувач"

