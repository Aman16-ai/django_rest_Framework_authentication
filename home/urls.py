from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
    path('',views.api_list,name='api_list'),
    path('task-list',views.taskList,name='taskList'),
    path('Detail-list/<str:pk>',views.DetailList,name='DetailList'),
    path('create',views.Create,name="create"),
    path('task-update/<str:pk>',views.taskUpdate,name="taskUpdate"),
    path('task-delete/<str:pk>',views.deleteTask,name="deleteTask"),
    path('signup',views.getMessage,name="signup"),
    path("register",views.registerUser,name="register"),
    path('login',views.loginUser,name='loginuser')
]
