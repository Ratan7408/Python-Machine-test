from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project_name', 'client', 'created_by', 'created_at']
    list_filter = ['client', 'created_at', 'updated_at']
    search_fields = ['project_name', 'client__client_name']
    readonly_fields = ['created_at', 'updated_at']
    filter_horizontal = ['users']
