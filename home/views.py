from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    """Home page view using template"""
    return render(request, 'home/home.html')

def welcome(request):
    """Simple welcome page with hardcoded HTML"""
    return HttpResponse("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Welcome to Django REST API</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
                background-color: #f5f5f5;
            }
            .container {
                background-color: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }
            h1 {
                color: #333;
                text-align: center;
                margin-bottom: 30px;
            }
            .nav-links {
                text-align: center;
                margin: 20px 0;
            }
            .nav-links a {
                display: inline-block;
                margin: 10px;
                padding: 10px 20px;
                background-color: #007bff;
                color: white;
                text-decoration: none;
                border-radius: 5px;
                transition: background-color 0.3s;
            }
            .nav-links a:hover {
                background-color: #0056b3;
            }
            .info {
                background-color: #e9ecef;
                padding: 20px;
                border-radius: 5px;
                margin: 20px 0;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🎉 Django REST API Project</h1>
            
            <div class="nav-links">
                <a href="/admin/">🔧 Admin Panel</a>
                <a href="/api/clients/">👥 Clients API</a>
                <a href="/api/projects/">📋 Projects API</a>
            </div>
            
            <div class="info">
                <h3>🚀 Your Django REST API is Ready!</h3>
                <p>This project implements a complete REST API system for managing Users, Clients, and Projects.</p>
                <ul>
                    <li><strong>Users:</strong> Use Django's built-in User model and admin panel</li>
                    <li><strong>Clients:</strong> Full CRUD operations via REST API</li>
                    <li><strong>Projects:</strong> Create projects and assign users</li>
                    <li><strong>Authentication:</strong> Session-based authentication</li>
                </ul>
            </div>
            
            <div class="info">
                <h3>📋 Quick Links:</h3>
                <ul>
                    <li><strong>Admin Panel:</strong> <a href="/admin/">http://127.0.0.1:8000/admin/</a></li>
                    <li><strong>API Base URL:</strong> <code>http://127.0.0.1:8000/api/</code></li>
                </ul>
            </div>
        </div>
    </body>
    </html>
    """)
