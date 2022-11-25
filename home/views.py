import profile
from unittest import expectedFailure
from attr import validate
from django.db.models import manager
from django.http import response
from django.shortcuts import render,HttpResponse
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from rest_framework.utils import serializer_helpers
from home.serializers import TaskSerializers, UserSerializers,UserProfileSerializer
from rest_framework.permissions import IsAuthenticated
from home.models import Task,UserProfile
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.
@api_view(['GET'])
def api_list(request):
    api_urls = {
        "List":'/task-list/',
        "Detail View":"/task-detail/<str:pk>/",
        "Create":"/task-create/",
        'update':"/task-update/<str:pk>",
        'Delete':"/task-delete/<str:pk>"
    }
    return Response(api_urls)
@api_view(['GET'])
def taskList(request):
    task = Task.objects.all()
    serializer = TaskSerializers(task,many=True)
    return Response(serializer.data)

@api_view(["GET"])
def DetailList(request,pk):
    task = Task.objects.get(pk=pk)
    serializer = TaskSerializers(task)
    return Response(serializer.data)
@api_view(['POST'])
def Create(request):
    serializer = TaskSerializers(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['POST'])
def taskUpdate(request,pk):
    task = Task.objects.get(pk = pk)
    serializer = TaskSerializers(instance=task,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteTask(request,pk):
    task = Task.objects.get(pk = pk)
    task.delete()
    return response.JsonResponse("Deleted")

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getMessage(request):
    print(f"The user id : {request.user.id}")
    return Response({"message":"hello you are authenticated"})




def generate_token(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh' : str(refresh),
        'access' : str(refresh.access_token)
    }

@api_view(['POST'])
def registerUser(request):
   try: 
        # username = request.data['username']
        # firstname = request.data['firstname']
        # lastname = request.data['lastname']
        # email = request.data['email']
        # password = request.data['password']
        
        # user = User.objects.create_user(username,email,password)
        # user.first_name = firstname
        # user.lastname = lastname
        # user.save()
        
#         userSer = UserSerializers
#         if userSer.is_valid():
#             userSer.save()
#             return Response("register successfully")
#         else:
#             return Response("register unsuccessfully")

    serializer = UserProfileSerializer(data = request.data)
    if serializer.is_valid(raise_exception=ValueError):
        student = serializer.create(validated_data=request.data)
        token = generate_token(student)
        return Response(token)
    
    return Response({"failed to create profile"})
    
            
   except Exception as e:
       print(str(e))
       return Response({"error": "something went wrong"})


    
@api_view(['POST'])
def loginUser(request):
    pass
    