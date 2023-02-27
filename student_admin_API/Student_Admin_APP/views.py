from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from Student_Admin_APP.models import Student_administration
from Student_Admin_APP.serializers import Student_administration_Serializer


# Create your views here.
@csrf_exempt
def student_administration_Api(request,id=0):
    if request.method=='GET':
        student_administrations = Student_administration.objects.all()
        student_administration__serializer = Student_administration_Serializer(student_administrations,many=True)
        return JsonResponse(student_administration__serializer.data,safe=False)
    elif request.method=='POST':
        student_administration_data = JSONParser().parse(request)
        student_administration__serializer = Student_administration_Serializer(data=student_administration_data)
        if student_administration__serializer.is_valid():
            student_administration__serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method == 'PUT':
        student_administration_data = JSONParser().parse(request)
        student_administration = Student_administration.objects.get(Student_administration_Id = student_administration_data['Student_administration_Id'])
        student_administration__serializer = Student_administration_Serializer(student_administration,data=student_administration_data)
        if student_administration__serializer.is_valid():
            student_administration__serializer.save()
            return JsonResponse("Update Successfully",safe=False)
        return JsonResponse("Failed to Update",safe=False)
    elif request.method == 'DELETE':
        student_administration = Student_administration.objects.get(Student_administration_Id=id)
        student_administration.delete()
        return JsonResponse("Deleted Succefully")
    