from django.contrib import admin
from django.urls import path
from Store import views
urlpatterns = [
    path('', views.index, name="index"),
    path('order', views.order, name="order"),
    path('signup', views.signup, name="signup"),
]
