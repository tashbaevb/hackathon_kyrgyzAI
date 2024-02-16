from rest_framework.response import Response
from rest_framework import generics, permissions, views

from . import models as m, serializers as s


class TaskListAPIView(generics.ListAPIView):
    queryset = m.Task.objects.all()
    serializer_class = s.TaskSerializer
    permission_classes = [permissions.IsAuthenticated]


class TaskDetailAPIView(generics.RetrieveAPIView):
    queryset = m.Task.objects.all()
    serializer_class = s.TaskSerializer
    permission_classes = [permissions.IsAuthenticated]


class ExampleListAPIView(generics.ListAPIView):
    queryset = m.Example.objects.all()
    serializer_class = s.ExampleSerializer
    permission_classes = [permissions.IsAuthenticated]


class ExampleDetailAPIView(generics.RetrieveAPIView):
    queryset = m.Example.objects.all()
    serializer_class = s.ExampleSerializer
    permission_classes = [permissions.IsAuthenticated]
