from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.new_user, name='new_user'),
    path('excel/', views.excel_data, name='excel_data'),
    path('helloworld/', views.insert, name='insert'),
]
