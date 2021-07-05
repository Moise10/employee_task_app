from django.urls import path
from .views import EmployeeDetailView,EmployeeListView,EmployeeDeleteView,EmployeeCreateView, EmployeeUpdateView

app_name = 'employee_app'

urlpatterns = [
    path('', EmployeeListView.as_view(), name="employee_list"),
    path('<int:pk>/', EmployeeDetailView.as_view(), name="employee_detail"),
    path('<int:pk>/update/', EmployeeUpdateView.as_view(), name="employee_update"),
    path('<int:pk>/delete/', EmployeeDeleteView.as_view(), name="employee_delete"),
    path('create_employee/', EmployeeCreateView.as_view(), name="employee_create")
]
