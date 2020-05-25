from django.contrib import admin
from django.urls import path
from . import views
#đừng quên import views (chỗ đựng function)

#This file find the patter that users type to the browser. 
#Path=> trigger that function and return the page

#The function 


urlpatterns = [
    path('', views.home, name="Dashboard"),
    path('vocabulary_list/', views.word, name="Vocabulary list"),
    path('student/<str:pk>/', views.student, name="student"),
    path('create_lesson/',views.createLesson, name="create_lesson")
]