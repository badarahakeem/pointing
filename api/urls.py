from django.urls import path
from api import views

urlpatterns = [
    path('pointage/', views.pointage_list),
    path('employee/', views.employee_list),
     path('login/', views.LoginView.as_view()),
    
]
