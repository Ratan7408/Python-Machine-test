from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.db import connection
import os

def home(request):
    """Home page view - returns template"""
    return render(request, 'home/home.html')

def welcome(request):
    """Welcome page with hardcoded HTML"""
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Django REST API - Welcome</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            .container { max-width: 800px; margin: 0 auto; }
            .header { background: #007bff; color: white; padding: 20px; border-radius: 5px; }
            .section { margin: 20px 0; padding: 20px; border: 1px solid #ddd; border-radius: 5px; }
            .endpoint { background: #f8f9fa; padding: 10px; margin: 10px 0; border-radius: 3px; }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Django REST API</h1>
                <p>Welcome to the Python Machine Test Project</p>
            </div>
            
            <div class="section">
                <h2>Available Endpoints</h2>
                <div class="endpoint">
                    <strong>GET /api/clients/</strong> - List all clients
                </div>
                <div class="endpoint">
                    <strong>POST /api/clients/</strong> - Create a new client
                </div>
                <div class="endpoint">
                    <strong>GET /api/projects/</strong> - List all projects
                </div>
                <div class="endpoint">
                    <strong>POST /api/clients/{id}/projects/</strong> - Create project for client
                </div>
            </div>
            
            <div class="section">
                <h2>Admin Panel</h2>
                <p><a href="/admin/">Access Admin Panel</a></p>
            </div>
        </div>
    </body>
    </html>
    """
    return JsonResponse({'html': html_content})

@csrf_exempt
def health_check(request):
    """Health check endpoint for Vercel"""
    return JsonResponse({
        'status': 'healthy',
        'message': 'Django REST API is running',
        'timestamp': '2025-08-08T22:00:00Z'
    })

@csrf_exempt
def api_status(request):
    """API status endpoint for Vercel"""
    try:
        # Try to connect to database
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        db_status = "connected"
    except Exception as e:
        db_status = f"error: {str(e)}"
    
    return JsonResponse({
        'api_status': 'operational',
        'database': db_status,
        'environment': os.environ.get('VERCEL_ENV', 'local'),
        'message': 'API endpoints are available'
    })
