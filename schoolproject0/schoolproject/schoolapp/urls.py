from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('application_form', views.application_form, name='application_form'),
    path('logout', views.logout, name='logout'),
    path('last_page', views.last_page, name='last_page'),
]