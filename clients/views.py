from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Client
from .serializers import ClientSerializer, ClientDetailSerializer

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def client_list(request):
    """List all clients or create a new client"""
    if request.method == 'GET':
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def client_detail(request, pk):
    """Retrieve, update or delete a client"""
    client = get_object_or_404(Client, pk=pk)
    
    if request.method == 'GET':
        serializer = ClientDetailSerializer(client)
        return Response(serializer.data)
    
    elif request.method in ['PUT', 'PATCH']:
        serializer = ClientSerializer(client, data=request.data, partial=request.method == 'PATCH')
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
