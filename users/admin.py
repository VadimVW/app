from django.contrib import admin

from carts.admin import CartTabAdmin
from users.models import User

# admin.site.register(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'username',]
    search_fields = ['username', 'first_name', 'last_name', 'email']
    # fields = 'username', 'first_name', 'last_name', 'email'

    inlines = [CartTabAdmin,]
