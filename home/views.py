from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.db import connection

def home(request):
    """Home page view"""
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
            code { background: #e9ecef; padding: 2px 4px; border-radius: 3px; }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>🚀 Django REST API Project</h1>
                <p>Welcome to your Django REST API with Clients and Projects management</p>
            </div>
            
            <div class="section">
                <h2>📋 Available Endpoints</h2>
                
                <div class="endpoint">
                    <h3>🏠 Home Page</h3>
                    <code>GET /</code> - This welcome page
                </div>
                
                <div class="endpoint">
                    <h3>💚 Health Check</h3>
                    <code>GET /health/</code> - API health status
                </div>
                
                <div class="endpoint">
                    <h3>📊 API Status</h3>
                    <code>GET /api/status/</code> - Database and API status
                </div>
            </div>
            
            <div class="section">
                <h2>🚀 Deployment</h2>
                <p>This project is configured for deployment on Vercel with:</p>
                <ul>
                    <li>✅ Django REST Framework</li>
                    <li>✅ Serverless architecture</li>
                    <li>✅ Static file handling</li>
                    <li>✅ Health monitoring</li>
                    <li>✅ API endpoints</li>
                </ul>
            </div>
        </div>
    </body>
    </html>
    """
    return JsonResponse({'message': 'Welcome to Django REST API', 'html': html_content})

@csrf_exempt
def health_check(request):
    """Health check endpoint for Vercel"""
    return JsonResponse({
        'status': 'healthy',
        'message': 'Django REST API is running',
        'version': '1.0.0',
        'environment': 'vercel'
    })

@csrf_exempt
def api_status(request):
    """API status endpoint to check database connectivity"""
    try:
        # Test database connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            db_status = "connected"
    except Exception as e:
        db_status = f"error: {str(e)}"
    
    return JsonResponse({
        'status': 'operational',
        'database': db_status,
        'message': 'API is running on Vercel',
        'environment': 'serverless'
    })
