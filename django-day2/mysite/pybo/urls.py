from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('<int:question_id>/', views.detail)
    #127.0.0.1:8000/pybo/1=> 127.0.0.1:8000/pybo/<int:question_id>/


]