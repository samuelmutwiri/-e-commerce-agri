from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('account/', views.account_view, name='account'),
    path('dynamic/', views.dynamic_content_view, name='dynamic_content_view'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
