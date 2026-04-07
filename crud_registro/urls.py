from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create_register, name='create_register'),
    path('update/<int:id>', views.update_register, name='update_register'),
    path('delete/<int:id>', views.delete_register, name='delete_register'),
]
