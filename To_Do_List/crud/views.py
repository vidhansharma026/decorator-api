from django.shortcuts import render
from . models import *
from . serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def AllData(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def OneData(request, pk):
    tasks = Task.objects.get(pk = pk)
    serializer = TaskSerializer(tasks)
    return Response(serializer.data)

@api_view(['POST'])
def CreateData(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def UpdateData(request, pk):
    tasks = Task.objects.get(pk=pk)
    serializer = TaskSerializer(data=request.data, instance=tasks)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def DeleteData(request, pk):
    tasks = Task.objects.get(pk=pk)
    tasks.delete()
    return Response('Deleted Successfully')

# @api_view(['DELETE'])
# def DelData(request, pk):
#     tasks = Task.objects.get(pk = pk).delete()
#     serializer = TaskSerializer(tasks)
#     return Response(serializer.data)


