from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Employee(models.Model):
    user = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True,blank=True)
    role = models.CharField(max_length=50, choices=[
        ('manager', 'Manager'),
        ('employee', 'Employee')
    ])

    def __str__(self):
        return self.user

'''class Employees(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    role = models.CharField(
        max_length=50,
        choices=[
            ('manager', 'Manager'),
            ('employee', 'Employee')
        ]
    )

    def __str__(self):
        return self.name
   ''' 
    
class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    manager = models.ForeignKey(Employee, on_delete=models.CASCADE)
    department = models.ManyToManyField(Department, related_name='projects')
    employees = models.ManyToManyField(Employee, related_name='projects')

    def __str__(self):
        return self.name


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    assigned_to = models.ForeignKey(Employee, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    STATUS_CHOICES=[
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed')
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES
        
    )
    
    
    def __str__(self):
        return self.title
    
'''class Personal(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.SET_NULL,null=True,blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True,blank=True)
    role = models.CharField(max_length=50, choices=[
        ('manager', 'Manager'),
        ('employee', 'Employee')
    ])

    def __str__(self):
        return self.user.username

'''