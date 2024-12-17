from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('register',views.register, name = 'register'),
    path('login',views.login, name = 'login'),
    path('logout',views.logout, name = 'logout'),
    path('dashboard',views.dashboard, name = 'dashboard'),
    path('createRecord',views.createRecord, name = 'createRecord'),
    path('updaterecords/<int:pk>',views.updaterecords, name = 'updaterecords'),
    path('delete/<int:pk>',views.delete, name = 'delete'),
    path('viewsrecord/<int:pk>',views.viewsrecord, name = 'viewsrecord'),
    path('index', views.index, name='index'),
    

]