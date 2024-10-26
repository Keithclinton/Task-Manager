from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.TaskListCreateView.as_view(), name='task-list-create'),  # URL for listing and creating tasks
    path('tasks/<int:pk>/', views.TaskDetailView.as_view(), name='task-detail'),  # URL for a specific task detail
]
