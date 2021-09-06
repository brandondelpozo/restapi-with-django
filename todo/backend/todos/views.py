from rest_framework import generics, serializers
from .models import Todo
from .serializers import TodoSeriliazer

class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSeriliazer


class DetailTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializers_class = TodoSeriliazer