from django.urls import path
from orders import views


urlpatterns = [
    path('', views.index, name='index'),
    path('orders/', views.orders, name='orders'),
    path('customers/', views.customers, name='customers'),
]