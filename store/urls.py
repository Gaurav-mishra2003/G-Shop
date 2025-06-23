from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
  path('',views.home,name='home'),
  path('/login',views.login_user,name='login'),
  path('/register',views.register,name='register'),
  path('/logout',views.logout_user,name='logout'),

# single product view
path('product/<int:pk>',views.product_view,name='product_view'),

  path('/about',views.about,name='about'),
  path('/category',views.category,name='category'),
]
