from django.contrib import admin
from django.urls import path
from . import views
#đừng quên import views (chỗ đựng function)

#This file find the patter that users type to the browser. 
#Path=> trigger that function and return the page

#The function 


urlpatterns = [
    path('', views.home, name="Dashboard"),
    path('task_list/', views.word, name="Vocabulary list"),
    path('member/<str:pk>/', views.student, name="student"),
    path('create_task/',views.createLesson, name="create_lesson"),
    path('add_member/',views.addStudent, name="add_student"),
    path('vocab_detail/<str:pk>/',views.vocab_detail, name="vocab_detail"),
    path('update_task/<str:pk>/', views.updateLesson, name="update_lesson"),
    path('delete_task/<str:pk>/', views.deleteLesson, name="delete_lesson"),


]

# ]

# urlpatterns = [
#     path('', views.home, name="Dashboard"),
#     path('vocabulary_list/', views.word, name="Vocabulary list"),
#     path('student/<str:pk>/', views.student, name="student"),
#     path('create_lesson/',views.createLesson, name="create_lesson"),
#     path('add_student/',views.addStudent, name="add_student"),
#     path('vocab_detail/<str:pk>/',views.vocab_detail, name="vocab_detail"),
#     path('update_task/<str:pk>/', views.updateOrder, name="update_order"),
#     path('delete_task/<str:pk>/', views.deleteOrder, name="delete_order"),


# ]

# ]