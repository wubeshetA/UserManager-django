from django.contrib import admin

# Register your models here.
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # display all fields
    list_display = [field.name for field in User._meta.fields]
    list_display_links = ('id', 'username')
    search_fields = ('username', 'first_name', 'last_name')
    list_per_page = 10