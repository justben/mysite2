from django.urls import path, include
from login import views

urlpatterns = [
	path("log_in/", views.log_in),
    path('', views.main_page),
    path('log_out/', views.log_out),
    path('test/', views.test)
]