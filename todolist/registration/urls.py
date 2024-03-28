from django.urls import path
from .views import Register, UserLogin, Create_Todolist

urlpatterns = [
    path('register/', Register.as_view(), name='UserRegistration'),
    path('userlogin/', UserLogin.as_view(), name='UserLogin'),
    path('usertodolist/', Create_Todolist.as_view(), name='TodoList'),
]
