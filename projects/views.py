from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Project
from .serializers import ProjectSerializer, ProjectCreateSerializer
from clients.models import Client

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def project_list(request):
    """List all projects assigned to the logged-in user"""
    user_projects = Project.objects.filter(users=request.user)
    serializer = ProjectSerializer(user_projects, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_project_for_client(request, client_id):
    """Create a new project for a specific client"""
    serializer = ProjectCreateSerializer(
        data=request.data,
        context={'client_id': client_id, 'request': request}
    )
    if serializer.is_valid():
        project = serializer.save()
        # Return the project with full details
        response_serializer = ProjectSerializer(project)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
