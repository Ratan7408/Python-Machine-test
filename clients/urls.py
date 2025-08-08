from django.urls import path
from . import views

urlpatterns = [
    path('', views.client_list, name='client-list'),
    path('<int:pk>/', views.client_detail, name='client-detail'),
] 