# mnc/urls.py

from django.urls import path
from .views import dashboard ,add_project,delete_project,edit_project , add_employee,employee_list ,add_department,add_task,assign_employees,delete_employee

urlpatterns = [
    path('',dashboard , name='dashboard'),
    path('add_project/',add_project ,name='add_project'),
    path('delete_project/<int:id>/', delete_project, name='delete_project'),
    path('edit_project/<int:id>/', edit_project, name='edit_project'),
    path('add_employee/', add_employee, name='add_employee'),
    path('employees/', employee_list, name='employee_list'),
    path('add_department/', add_department, name='add_department'),
    path('add_task/', add_task, name='add_task'),
    path('assign_employees/<int:project_id>/', assign_employees, name='assign_employees'),
    path('delete_employee/<int:id>/', delete_employee, name='delete_employee'),
    
    
]