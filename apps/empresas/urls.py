from django.contrib import admin
from django.urls import path
from .views import EmpresaCreat, EmpresaEdit


urlpatterns = [
    path('/novo', EmpresaCreat.as_view(), name='create_empresa'),
    path('editar/<int:pk>/', EmpresaEdit.as_view(), name='edit_empresa'),
]