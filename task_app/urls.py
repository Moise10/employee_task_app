from django.urls import path
from .views import TaskDetailView, TaskListView, TaskUpdateView, TaskDeleteView, TaskCreateView, AssignEmployee, TaskCategoryView, TaskCategoryDetail

app_name="task-app"

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('<int:pk>/',TaskDetailView.as_view(), name='task_detail'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('<int:pk>/assign_task/', AssignEmployee.as_view(), name='assign_task'),
    path('create/', TaskCreateView.as_view(), name='create_task'),
    path('categories/', TaskCategoryView.as_view(), name='task_categories'),
    path('categories/<int:pk>/', TaskCategoryDetail.as_view(),name='category_detail'),
    
]
