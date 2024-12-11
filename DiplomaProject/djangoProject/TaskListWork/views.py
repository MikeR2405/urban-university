from rest_framework import generics, permissions
from .models import Task
from .serializers import TaskSerializer
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.utils.timezone import make_aware  # Импортируем make_aware
import datetime


class TaskListView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


def index_view(request):
    tasks = Task.objects.all()
    return render(request, 'TaskListWork/index.html', {'tasks': tasks})


@login_required
def task_create_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')

        if due_date:
            # Преобразуем строку в дату и делаем её осведомленной
            due_date = datetime.datetime.strptime(due_date, '%Y-%m-%d')
            due_date = make_aware(due_date)  # Делаем дату осведомленной

            # Теперь можно безопасно сравнивать
            if due_date < timezone.now():
                return render(request, 'TaskListWork/task_form.html', {'error': 'Due date must be in the future.'})

        # Создание задачи для аутентифицированного пользователя
        task = Task.objects.create(title=title, description=description, due_date=due_date, user=request.user)
        return redirect('task_list')

    return render(request, 'TaskListWork/task_form.html')


@login_required
def task_delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    # Проверка, что пользователь является владельцем задачи
    if request.user == task.user:
        task.delete()
    return redirect('task_list')  # После удаления перенаправление на список задач
