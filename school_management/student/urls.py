from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='student-landing'),
    path('<int:identifier>/', views.dashboard, name='student-dashboard'),
    path('add/', views.add)
]
