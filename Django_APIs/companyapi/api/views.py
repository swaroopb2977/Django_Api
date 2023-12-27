from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company,Employee
from rest_framework.decorators import action
from api.serializers import CompanySerializer,EmployeeSerializer
from rest_framework.response import Response
# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer
    
    
    #companies/{companyId}/employees
    @action(detail=True,methods=['get'])
    def employees(Self,request,pk=None):
        
        company=Company.objects.get(pk=pk)
        emps=Employee.objects.filter(company=company)
        emps_serializer=EmployeeSerializer(emps,many=True,context={'request':request})
        #print("get employees of ",pk,"company")
        return Response(emps_serializer.data)
    
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer