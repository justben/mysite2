from django.urls import path, include
from login import views

urlpatterns = [
	path("sign_in/", views.signin),
	path("sign_out/", views.signout),
    path('main_page/', views.main_page),
    path('hello/', views.hello)
]