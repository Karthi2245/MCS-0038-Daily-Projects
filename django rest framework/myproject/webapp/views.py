from django.shortcuts import render
from django.http import HttpResponse  # for including http methods
from django.shortcuts import get_object_or_404  # content not found
from rest_framework.views import APIView
from rest_framework.decorators import api_view  # function based view
from rest_framework.response import Response  # getting response
from rest_framework import status  # getting content status
from .models import Employee
from .serializers import EmployeeSerializers  # to get the serializers class
# Create your views here.


class EmployeeList(APIView):

    def get(self, request):
        employee1 = Employee.objects.all()  # getting data from models
        serializer = EmployeeSerializers(employee1, many=True)  # coverting the models to json
        return Response(serializer.data)

    def post(self,request):
        # employee1 = Employee.objects.all()  # getting data from models
        serializer = EmployeeSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


class EmployeeDetail(APIView):

    def get_object(self, id):
        emp = Employee.objects.get(id= id)
        return emp

    def get(self, request, id ):
        emp = self.get_object(id)
        serializer = EmployeeSerializers(emp)
        return Response(serializer.data)

    def put(self, request, id):
        emp = self.get_object(id)
        serializer = EmployeeSerializers(emp, data= request.data)
        if serializer .is_valid():
            serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        emp = self.get_object(id)
        emp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# @api_view(['POST'])
# def update(request,id):
#     employee2 = Employee.objects.get(id=id)
#     serializer = EmployeeSerializers(instance=employee2,data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

    # def delete(self, request,id):
    #     employee2 = Employee.objects.get(id=id)
    #     serializer = EmployeeSerializers(employee1, data=request.data)
    #     del serializer
    #     return Response(serializer.data)

























































































