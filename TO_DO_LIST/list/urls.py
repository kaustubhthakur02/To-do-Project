from django.contrib import admin
from django.urls import path,include
from list import views

urlpatterns = [
    path("",views.login, name = "login"),
    path('cr/', views.create, name = "index1"),
    path('sh/',views.show, name ="index2"),
    path('delete/<rid>', views.delete, name = "delete"),
    path('edit/<rid>', views.edit, name = "edit"),
]