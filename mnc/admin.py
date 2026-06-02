from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Department, Employee, Project, Task

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'department') 
    
admin.site.register(Department)
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Project)
admin.site.register(Task)