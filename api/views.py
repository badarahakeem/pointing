from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from eqrApp.models import Employee, Pointing
from api.serializers import CheckEmpForm, EmployeeSerlializer, PointingSerlializer
import datetime
from django.utils import timezone

# Create your views here.


@api_view(['GET', 'POST'])
def employee_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Employee.objects.all()
        serializer = EmployeeSerlializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = EmployeeSerlializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def pointage_list(request):
    
    if request.method == 'GET':
        snippets = Pointing.objects.all()
        serializer = PointingSerlializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CheckEmpForm(data=request.data)
        if serializer.is_valid():
            id_in = request.data['id']
            employee = Employee.objects.filter(employee_code = id_in).first()
            point = Pointing.objects.filter(employee__employee_code = id_in).last()

            # checking
            if point is not None:
                time_leave = (point.created + datetime.timedelta(hours=10))

                
                if not point.clock_out and timezone.now() < (point.created + datetime.timedelta(hours=10)):
                
                    if timezone.now() < time_leave:
                        print(id_in)
                        Pointing.objects.filter(employee__employee_code = id_in).update(clock_out=timezone.now())
                        print('the 1')
                    

                else:
                    if  not timezone.now() < (point.created + datetime.timedelta(hours=20)):
                        
                        employee = Employee.objects.filter(employee_code = id_in).first()
                        Pointing.objects.create(employee=employee, clock_time=timezone.now())
                        print('the 3')
                    
                
            else:
                Pointing.objects.create(employee_id=employee.id, clock_time=timezone.now())
                print('the 4')

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)