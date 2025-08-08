from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

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
                    <h3>⚙️ Admin Panel</h3>
                    <code>GET /admin/</code> - Django admin interface<br>
                    <strong>Username:</strong> admin<br>
                    <strong>Password:</strong> admin
                </div>
                
                <div class="endpoint">
                    <h3>👥 Clients API</h3>
                    <code>GET /api/clients/</code> - List all clients<br>
                    <code>POST /api/clients/</code> - Create new client<br>
                    <code>GET /api/clients/{id}/</code> - Get specific client<br>
                    <code>PUT /api/clients/{id}/</code> - Update client<br>
                    <code>DELETE /api/clients/{id}/</code> - Delete client
                </div>
                
                <div class="endpoint">
                    <h3>📁 Projects API</h3>
                    <code>GET /api/projects/</code> - List user's projects<br>
                    <code>POST /api/clients/{client_id}/projects/</code> - Create project for client
                </div>
                
                <div class="endpoint">
                    <h3>💚 Health Check</h3>
                    <code>GET /health/</code> - API health status
                </div>
            </div>
            
            <div class="section">
                <h2>🔧 API Usage Examples</h2>
                
                <h3>Create a Client:</h3>
                <pre><code>curl -X POST http://localhost:8000/api/clients/ \\
  -H "Content-Type: application/json" \\
  -d '{"client_name": "Tech Corp"}'</code></pre>
                
                <h3>Create a Project:</h3>
                <pre><code>curl -X POST http://localhost:8000/api/clients/1/projects/ \\
  -H "Content-Type: application/json" \\
  -d '{"project_name": "Website Redesign"}'</code></pre>
            </div>
            
            <div class="section">
                <h2>🚀 Deployment</h2>
                <p>This project is configured for deployment on Vercel with:</p>
                <ul>
                    <li>✅ Django REST Framework</li>
                    <li>✅ SQLite database</li>
                    <li>✅ Static file handling</li>
                    <li>✅ Admin interface</li>
                    <li>✅ API authentication</li>
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
        'version': '1.0.0'
    })
