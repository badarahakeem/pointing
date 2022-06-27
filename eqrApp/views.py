from datetime import datetime , timedelta
from django.utils import timezone
from django.shortcuts import redirect, render
import datetime
import json
from django.contrib import messages
from django.http import HttpResponse
from eqrApp import models, forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from eqrApp.models import Employee, Pointing
from structures.models import Agent, Society



def context_data():
    context = {
        'page_name' : '',
        'page_title' : 'Chat Room',
        'system_name' : 'ID d\'employé avec générateur de code QR',
        'topbar' : True,
        'footer' : True,
    }

    return context


# Create your views here.
def login_page(request):
    context = context_data()
    context['topbar'] = False
    context['footer'] = False
    context['page_name'] = 'login'
    context['page_title'] = 'Connexion'
    return render(request, 'login.html', context)

def login_user(request):
    logout(request)
    resp = {"status":'failed','msg':''}
    username = ''
    password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                resp['status']='success'
            else:
                resp['msg'] = "Incorrect username or password"
        else:
            resp['msg'] = "Incorrect username or password"
    return HttpResponse(json.dumps(resp),content_type='application/json')

@login_required
def home(request):
    context = context_data()
    context['page'] = 'home'
    context['page_title'] = 'Home'
    context['employees'] = models.Employee.objects.count()
    return render(request, 'home.html', context)

def logout_user(request):
    logout(request)
    return redirect('login-page')


@login_required
def employee_list(request):
    agent_id = Agent.objects.get(user = request.user)
    sos_id = Society.objects.filter(id = agent_id.society_id.id)
    print(sos_id)
    context =context_data()
    context['page'] = 'employee_list'
    context['page_title'] = 'Liste des Employés'
    context['employees'] = models.Employee.objects.filter(agent__society_id = sos_id[0])

    return render(request, 'employee_list.html', context)

@login_required 
def manage_employee(request, pk=None):
    context =context_data()
    if pk is None:
        context['page'] = 'add_employee'
        context['page_title'] = 'Ajouter un employé'
        context['employee'] = {}
    else:
        context['page'] = 'edit_employee'
        context['page_title'] = 'Mise a jour '
        context['employee'] = models.Employee.objects.get(id=pk)

    return render(request, 'manage_employee.html', context)

@login_required
def save_employee(request):
    agent_id = Agent.objects.get(user = request.user)
    print(agent_id)
    resp = { 'status' : 'failed', 'msg' : '' }
    if not request.method == 'POST':
        resp['msg'] = "No data has been sent into the request."

    else:
        if request.POST['id'] == '':
            form = forms.SaveEmployee(request.POST, request.FILES)
        else:
            employee = models.Employee.objects.get(id = request.POST['id'])
            form = forms.SaveEmployee(request.POST, request.FILES, instance = employee)
        if form.is_valid():
            inst = form.save(commit=False)
            inst.agent = agent_id
            inst.save()
            if request.POST['id'] == '':
                messages.success(request, f"{request.POST.get('employee_code')} has been added successfully.")
            else:
                messages.success(request, f"{request.POST.get('employee_code')} has been updated successfully.")
            resp['status'] = 'success'
        else:
            for field in form:
                for error in field.errors:
                    if not resp['msg'] == '':
                        resp['msg'] += str("<br />")
                    resp['msg'] += str(f"[{field.label}] {error}")

    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def view_card(request, pk =None):
    if pk is None:
        return HttpResponse("Employee ID is Invalid")
    else:
        context = context_data()
        context['employee'] = models.Employee.objects.get(id=pk)
        return render(request, 'view_id.html', context)

@login_required
def view_scanner(request):
    context = context_data()
    return render(request, 'scanner.html', context)


@login_required
def view_details(request, code = None):
    if code is None:
        return HttpResponse("Employee code is Invalid")
    else:
        context = context_data()
        context['employee'] = models.Employee.objects.get(employee_code=code)
        return render(request, 'view_details.html', context)

@login_required
def delete_employee(request, pk=None):
    resp = { 'status' : 'failed', 'msg' : '' }
    if pk is None:
        resp['msg'] = "No data has been sent into the request."
    else:
        try:
            models.Employee.objects.get(id=pk).delete()
            resp['status'] = 'success'
            messages.success(request, 'Employee has been deleted successfully.')
        except:
            resp['msg'] = "Employee has failed to delete."

    return HttpResponse(json.dumps(resp), content_type="application/json")





#### Clock in/out #############################################################
@login_required
def clock_in(request):
    context = {}
    form = forms.IDForm()
    if request.method=="POST":
        form = forms.IDForm(request.POST or None)
        if form.is_valid():
            id_in = form.cleaned_data['id']
            # testing
            employee = Employee.objects.filter(employee_code = id_in).first()
            point = Pointing.objects.filter(employee__employee_code = id_in).last()
            print(point.clock_out)


            # checking
            if point is not None:
                time_leave = (point.created + datetime.timedelta(hours=10))

                
                if not point.clock_out and timezone.now() < (point.created + datetime.timedelta(hours=10)):
                
                    if timezone.now() < time_leave:
                        print(id_in)
                        Pointing.objects.filter(employee__employee_code = id_in).update(clock_out=timezone.now())
                        print('the 1')
                    

                else:
                    if  timezone.now() < (point.created + datetime.timedelta(hours=20)):
                        print('the 2')
                        return redirect('point-list')

                    else:
                        employee = Employee.objects.filter(employee_code = id_in).first()
                        Pointing.objects.create(employee=employee, clock_time=timezone.now())
                        print('the 3')
                    
                
            else:
                Pointing.objects.create(employee_id=employee.id, clock_time=timezone.now())
                print('the 4')

            return redirect('/')

    context['form']= form
    return render(request, "create_view.html", context)


@login_required
def point_list(request):
    context = context_data()
    context['page'] = 'point_list'
    context['page_title'] = 'Liste des Employés Pointés'
    context['points'] = models.Pointing.objects.all()

    return render(request, 'point_list.html', context)