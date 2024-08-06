from django.shortcuts import render
from django.urls import reverse_lazy
from tasking.models import Task
from django.views.generic import ListView, DetailView, CreateView
from tasking.forms import TaskForm

class TaskListView(ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "tasks/tasks.html"

class TaskDetailView(DetailView):
    model = Task
    context_object_name = "task"
    template_name = "tasks/task_details.html"

class TaskCreateView(CreateView):
    model = Task
    template_name = "tasks/task-form.html"
    form_class = TaskForm
    success_url = reverse_lazy("tasks:task-list")
