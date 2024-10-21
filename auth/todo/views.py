from django.shortcuts import render
from .models import Todo
from rest_framework import generics

from .serializers import TodoSerializer
# Create your views here.
class TodoListCreateView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
class TodoUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    partial = True
    
    
# class TodoDeleteView(generics.DestroyAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer

#     def destroy(self, request, *args, **kwargs):
#         instance = self.get_object()
#         self.perform_destroy(instance)
#         return Response({"message": "Todo deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

#     def perform_destroy(self, instance):
#         instance.delete()
class TodoDeleteView(generics.DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Todo deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()
