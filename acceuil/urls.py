from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('login',views.connexion),
    path('register',views.register)
]
