from django.urls import path
from django.contrib.auth import views as auth_views  # Импортируйте auth_views
from .views import index_view, TaskListView, task_create_view, task_delete_view

urlpatterns = [
    path('', index_view, name='task_list'),
    path('tasks/', TaskListView.as_view(), name='task_api'),
    path('tasks/create/', task_create_view, name='task_create'),
    path('tasks/delete/<int:pk>/', task_delete_view, name='task_delete'),
    path('login/', auth_views.LoginView.as_view(template_name='TaskListWork/registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='task_list'), name='logout'),
]
