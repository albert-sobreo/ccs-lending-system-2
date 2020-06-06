from django.urls import path, include
from app import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.borrow),
    path('return/', views.ret),
    path('register/', views.register),
    path('login/', views.login),
    path('logs/', views.logs),
    path('requests/', views.requests),
    path('register-process/', views.register_process),
    path('requestprocess/', views.request_process),
    path('request-success/<str:request_number>', views.request_success),
    path('return-success/', views.ret_success),
    path('return-process/', views.ret_process),
    path('ret-success/', views.ret_success),
    path('login-process/', views.login_process),
    path('logout/', views.logoutview),
    path('approve-process/<int:pk>', views.approve_process),
]