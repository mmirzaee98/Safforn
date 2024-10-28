from django.contrib import admin
from user.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'phone', 'national_id']
    list_filter = ['is_active','last_login','is_staff','date_joined']
    search_fields = ['username', 'first_name', 'last_name','phone','national_id']