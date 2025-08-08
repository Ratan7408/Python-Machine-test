"""
URL configuration for django_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home import views as home_views
from projects import views as project_views

urlpatterns = [
    path('', home_views.home, name='home'),     # Home page using template
    path('health/', home_views.health_check, name='health_check'),  # Health check for Vercel
    path('admin/', admin.site.urls),       # Admin panel
    
    # API endpoints
    path('api/clients/', include('clients.urls')),
    path('api/projects/', include('projects.urls')),
    path('api/clients/<int:client_id>/projects/', project_views.create_project_for_client, name='create-project-for-client'),
]
