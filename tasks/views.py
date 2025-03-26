from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Task
from .serializers import TaskSerializer

class TaskListCreateView(APIView):
    permission_classes = [IsAuthenticated]
    #permission_classes = [AllowAny]

    def get(self, request):
        tasks = Task.objects.filter(user=request.user)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        request.data["user"] = request.user.id
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, task_id, user):
        try:
            return Task.objects.get(id=task_id, user=user)
        except Task.DoesNotExist:
            return None

    def get(self, request, task_id):
        task = self.get_object(task_id, request.user)
        if task:
            serializer = TaskSerializer(task)
            return Response(serializer.data)
        return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, task_id):
        task = self.get_object(task_id, request.user)
        if task:
            serializer = TaskSerializer(task, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, task_id):
        task = self.get_object(task_id, request.user)
        if task:
            task.delete()
            return Response({"message": "Task deleted"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
