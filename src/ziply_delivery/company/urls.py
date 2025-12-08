from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='company_register'),
    path('<str:company_name>/create/', views.parcel_create, name='company_parcel_create'),
    path('<str:company_name>/', views.package, name='company_dashboard'),
]
