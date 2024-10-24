from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('login/', views.login_view, name='login'),
  path('register/', views.register, name='register'),
  path('order_coffee/', views.order_coffee, name='order_coffee'),
  path('drink_coffee/', views.drink_coffee, name='drink_coffee'),
  path('leave_cafe/', views.leave_cafe, name='leave_cafe'),
]
