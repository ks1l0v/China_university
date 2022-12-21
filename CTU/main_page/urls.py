from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('news/<int:pk>', views.news),
    path('send_com/<int:pk>', views.send_com),
]
