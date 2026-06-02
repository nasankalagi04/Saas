# Create your views here.
from django.shortcuts import render ,redirect , get_object_or_404
from .models import Department, Employee , Project , Task
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST


def dashboard(request):
    project= Project.objects.all()
    task = Task.objects.all()
    employees=Employee.objects.all()
    
    
    for proj in project:
        print(proj.employees.all())
    return render(request, 'mnc/dashboard.html', {'project': project ,'task':task,'employees':employees})


def add_project(request):
    manager = Employee.objects.filter(role='manager')
    employees = Employee.objects.filter(role='employee')
    department = Department.objects.all()
    
    
    if request.method == 'POST':
        name = request.POST.get('name')
        manager_id = request.POST.get('manager_id')
        department_id = request.POST.get('department_id')
        employee_ids = request.POST.getlist('employee_ids')
        
        
        #single object
        manager = Employee.objects.get(id=manager_id)
        'department = Department.objects.get(id=department_id)'
        
        #create project
        project=Project.objects.create(name=name , manager=manager)
        
        #multiple employee
        employees =Employee.objects.filter(id__in=employee_ids)
        
        #assign employee
        project.department.set(department_id)
        project.employees.set(employees)
        
        
        return redirect('dashboard')

    return render(request, 'mnc/add_project.html',{'employees': employees ,'manager': manager, 'department': department})
    
    

    
def delete_project(request, id):
    project = Project.objects.filter(id=id).first()
    
    if not project:
        return redirect('dashboard')
    
    if request.method == 'POST': 
        project.delete()
        return redirect('dashboard')
    return render(request, 'mnc/delete_project.html',{'project':project})

def edit_project(request, id):
    project = get_object_or_404(Project, id=id)

    if request.method == 'POST':
        project.name = request.POST.get('name')
        project.save()
        return redirect('dashboard')

    return render(request, 'mnc/edit_project.html', {'project': project})


def add_employee(request):
    departments = Department.objects.all()

    if request.method == 'POST':
        username = request.POST.get('username')
        
        department_id = request.POST.get('department_id')
        role = request.POST.get('role')

        # create user
        user = User.objects.create(username=username,  password="12345")
        user.save()

        # create employee
        department = Department.objects.get(id=department_id)

        Employee.objects.create(
            user=user,
            department=department,
            role=role
        )

        return redirect('dashboard')

    return render(request, 'mnc/add_employee.html', {
        'departments': departments
    })

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'mnc/employee_list.html', {
        'employees':employees
        
    })
    
    
def add_department(request):
    if request.method == 'POST':
        name = request.POST.get('name')

        if name:
            Department.objects.get_or_create(name=name)

        return redirect('dashboard')

    return render(request, 'mnc/add_department.html')

def add_task(request):
    projects = Project.objects.all()
    employees = Employee.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        project_id = request.POST.get('project_id')
        employee_ids = request.POST.get('employee_ids')

        project = Project.objects.get(id=project_id)
        employee = Employee.objects.get(id=employee_ids)

        Task.objects.create(
            title=title,
            project=project,
            assigned_to=employee
        )

        return redirect('dashboard')

    return render(request, 'mnc/add_task.html', {
        'projects': projects,
        'employees': employees
    })

def assign_employees(request, project_id):
    project = Project.objects.get(id=project_id)
    manager = Employee.objects.filter(role='manager')
    employees = Employee.objects.filter(role='employee')

    if request.method == 'POST':
        employee_ids = request.POST.getlist('employee_ids')

        # assign employees to project
        for empp_id in employee_ids:
         project.employees.add(empp_id)

        return redirect('dashboard')

    return render(request, 'mnc/assign_employees.html', {
        'project': project,'manager':manager,
        'employees': employees
    })

@require_POST
def delete_employee(request, id):
    user = get_object_or_404( Employee,id=id)
    user.delete()  # only employee
    return redirect('employee_list')
'''
@require_POST
def delete_user(request, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    return redirect('employee_list')'''