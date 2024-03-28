from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from .models import UserRegister, UserTodoList
from .serializers import UserRegisterSerializer, UserLoginSerializer, UserTodoListSerializer
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password, check_password
import hashlib


# Create your views here.
class Register(generics.GenericAPIView):
    serializer_class = UserRegisterSerializer
    queryset = UserRegister.objects.all()

    def post(self, request):
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        except UserRegister.DoesNotExist:
        # Handling the DoesNotExist exception
            return HttpResponse("Object does not exist.")
        except ValidationError as e:
            # Handling validation errors
            return HttpResponse("Validation error: {}".format(e))
        except Exception as e:
            # Handling any other unexpected exceptions
            return HttpResponse("An unexpected error occurred: {}".format(e))
        else:
            # Code to execute if no exception is raised
            return HttpResponse("Success: {}".format(obj))
        
    def get(self, request):
        try:
            user = UserRegister.objects.all()
            user_data = self.get_serializer(user, many=True)
            return Response(user_data.data, status=status.HTTP_201_CREATED)
        
        except UserRegister.DoesNotExist:
            # If the instance is not found, return a custom error message
            return Response({"error": "The requested resource does not exist."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            # Handle other exceptions and return a generic error message
            return Response({"error": "An unexpected error occurred."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class UserLogin(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        try:
            username = request.data.get('Username')
            password = request.data.get('Password')

            user = UserRegister.objects.get(Username=username)
            password1 = user.Password
            print(password1, 'one')
            if check_password(password, password1):
                return Response({'Result': user.id}, status=status.HTTP_200_OK)
                # return render(request, 'todo_lists.html')
        except Exception as e:
            # Handle other exceptions and return a generic error message
            return Response({"error": "An unexpected error occurred."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class Create_Todolist(generics.GenericAPIView):
    serializer_class = UserTodoListSerializer
    queryset = UserRegister.objects.all()

    def post(self, request):
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        except UserRegister.DoesNotExist:
        # Handling the DoesNotExist exception
            return HttpResponse("Object does not exist.")
        except ValidationError as e:
            # Handling validation errors
            return HttpResponse("Validation error: {}".format(e))
        except Exception as e:
            # Handling any other unexpected exceptions
            return HttpResponse("An unexpected error occurred: {}".format(e))
        else:
            # Code to execute if no exception is raised
            return HttpResponse("Success: {}".format(obj))