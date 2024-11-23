from django.urls import path
from todo import views

app_name="todo"

urlpatterns = [
    path('',views.todolist,name="todolist"),
    path('update_task/<str:pk>/',views.updateTask,name="update_task"),    
    path('delete/<str:pk>/',views.deleteTask,name="delete"),    
    path('checklist/<str:pk>/',views.checklist,name="checklist"),    
            ]