from django.urls import path
from . import views

urlpatterns = [
    path('', views.PageListCreateView.as_view(), name='page-list-create'),
    path('<str:pk>/', views.PageDetailView.as_view(), name='page-detail'),
]
