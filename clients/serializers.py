from rest_framework import serializers
from .models import Client
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='get_full_name')
    
    class Meta:
        model = User
        fields = ['id', 'name']

class ClientSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source='created_by.get_full_name', read_only=True)
    
    class Meta:
        model = Client
        fields = ['id', 'client_name', 'created_at', 'created_by', 'updated_at']
        read_only_fields = ['id', 'created_at', 'created_by', 'updated_at']

class ClientDetailSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source='created_by.get_full_name', read_only=True)
    projects = serializers.SerializerMethodField()
    
    class Meta:
        model = Client
        fields = ['id', 'client_name', 'projects', 'created_at', 'created_by', 'updated_at']
        read_only_fields = ['id', 'created_at', 'created_by', 'updated_at']
    
    def get_projects(self, obj):
        from projects.serializers import ProjectBasicSerializer
        return ProjectBasicSerializer(obj.projects.all(), many=True).data 