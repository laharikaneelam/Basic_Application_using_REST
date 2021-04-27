from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework .response import Response
from .models import employees
from .serializers import employeeSerializer

class employeeList(APIView):
    def get(self,request):
        employeel=employees.objects.all()
        serializer=employeeSerializer(employeel,many=True)
        return Response(serializer.data)
