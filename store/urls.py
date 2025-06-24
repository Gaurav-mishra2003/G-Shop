from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
  path('',views.home,name='home'),
  path('/login',views.login_user,name='login'),
  path('/register',views.register,name='register'),
  path('/logout',views.logout_user,name='logout'),
  path('update_user/', views.update_user, name='update_user'),
  path('update_info/', views.update_info, name='update_info'),
  path('search/', views.search, name='search'),

# single product view
path('product/<int:pk>',views.product_view,name='product_view'),

  path('/about',views.about,name='about'),
  path('/category',views.category,name='category'),
]
