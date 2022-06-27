from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, views, permissions
from eqrApp.models import Employee, Pointing
from structures import models
from api.serializers import CheckEmpForm, EmployeeSerlializer, PointingSerlializer, LoginSerializer
import datetime
from django.utils import timezone

from django.contrib.auth import login

# Create your views here.



class LoginView(views.APIView):
    # This view should be accessible also for unauthenticated users.
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = LoginSerializer(data=self.request.data,
            context={ 'request': self.request })
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(None, status=status.HTTP_202_ACCEPTED)




@api_view(['GET', 'POST'])
def employee_list(request):
    agent = models.Agent.objects.get(user=request.user)
    if agent.is_admin == True or agent.is_agent == True:
    
        if request.method == 'GET':
            snippets = Employee.objects.filter(agent__society_id = request.user.agent.society_id)
            serializer = EmployeeSerlializer(snippets, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = EmployeeSerlializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'POST'])
def pointage_list(request):
    agent = models.Agent.objects.get(user=request.user)
    if agent.is_admin == True or agent.is_agent == True:
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
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)





