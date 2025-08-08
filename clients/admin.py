from django.contrib import admin
from .models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'created_by', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['client_name']
    readonly_fields = ['created_at', 'updated_at']
