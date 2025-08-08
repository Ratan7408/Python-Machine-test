from rest_framework import serializers
from .models import Project
from django.contrib.auth.models import User
from clients.models import Client

class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='get_full_name')
    
    class Meta:
        model = User
        fields = ['id', 'name']

class ProjectBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'project_name']

class ProjectSerializer(serializers.ModelSerializer):
    client = serializers.CharField(source='client.client_name', read_only=True)
    users = UserSerializer(many=True, read_only=True)
    created_by = serializers.CharField(source='created_by.get_full_name', read_only=True)
    
    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'users', 'created_at', 'created_by']
        read_only_fields = ['id', 'client', 'created_at', 'created_by']

class ProjectCreateSerializer(serializers.ModelSerializer):
    users = serializers.ListField(
        child=serializers.IntegerField(),
        write_only=True,
        required=False
    )
    
    class Meta:
        model = Project
        fields = ['project_name', 'users']
    
    def create(self, validated_data):
        users_data = validated_data.pop('users', [])
        client_id = self.context['client_id']
        user = self.context['request'].user
        
        # Get the client
        try:
            client = Client.objects.get(id=client_id)
        except Client.DoesNotExist:
            raise serializers.ValidationError("Client not found")
        
        # Create the project
        project = Project.objects.create(
            **validated_data,
            client=client,
            created_by=user
        )
        
        # Assign users to the project
        if users_data:
            users = User.objects.filter(id__in=users_data)
            project.users.set(users)
        
        return project 