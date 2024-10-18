from django.shortcuts import render
from .models import Todo
from rest_framework import generics

from .serializers import TodoSerializer
# Create your views here.
class TodoListCreateView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
