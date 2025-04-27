from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='home'),
    path('single_product/<int:pk>/', views.single_product, name='single_product')
]
