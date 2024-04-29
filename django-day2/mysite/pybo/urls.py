
from django.urls import path
from . import views
app_name='pybo'

urlpatterns = [
    path('question/modify/<question_id>/',views.question_modify , name='question_modify'),
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/',views.question_create,name='question_create'),
    path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'),
    path('answer/modify/<int:answer_id>/', views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),



    #127.0.0.1:8000/pybo/1=> 127.0.0.1:8000/pybo/<int:question_id>/
]