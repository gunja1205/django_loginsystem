from django.urls import path 
from django.contrib import admin 
from django.contrib.auth import views as auth_views
from .views import index,register,login_user,logout_user,admin_login
# from .views import home

from . import views 
urlpatterns = [
    path('', views.index, name="index"),
    path("register", register, name="register"),
    path("login_user", login_user, name="login_user"),
    path("logout_user", logout_user, name="logout_user"),
    path("admin_login", admin_login ,name="admin_login"),
    path("search", views.search ,name="search"),

]
