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
    path('api/status/', home_views.api_status, name='api_status'),  # API status for Vercel
    
    # Note: Admin and database-dependent APIs are disabled for Vercel deployment
    # as the serverless environment doesn't support persistent SQLite databases
]
