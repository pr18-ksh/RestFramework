from django.shortcuts import render
from api.models import Student
from api.serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse
# Create your views here.

def student_detail(request,pk):
    std = Student.objects.get(id=pk)
    # print(std)
    serializer = StudentSerializer(std)
    # print(serializer)
    # print(serializer.data)
    # json_data= JSONRenderer().render(serializer.data)
    # print(json_data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data)

def student_list(request):
    std = Student.objects.all()
    serializer = StudentSerializer(std,many=True)
    # json_data= JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data,safe=False)
