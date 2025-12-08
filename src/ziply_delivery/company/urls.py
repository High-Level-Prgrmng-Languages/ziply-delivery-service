from django.urls import path
from . import views

urlpatterns = [
    path('<str:company_name>/', views.package, name='company'),
    path('<str:company_name>/create', views.parcel_create, name='company'),
    path('register', views.register, name='register')
]
