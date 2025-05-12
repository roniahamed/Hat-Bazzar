from django.urls import path
from . import views
app_name = 'shop'
urlpatterns = [
    path('',views.index, name='home'),
    path('product/<int:id>/', views.single_product, name='single_product'),
    path('checkout/', views.checkout, name='checkout')
]
