from django.shortcuts import render, reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
from .forms import TaskModelForm


class LandingPageView(generic.TemplateView):
  template_name = 'landing_page.html'


class TaskListView(LoginRequiredMixin,generic.ListView):
  template_name = 'task_app/task_list.html'
  context_object_name = 'tasks'

  def get_queryset(self):
    return Task.objects.order_by('-created_at')


class TaskDetailView(LoginRequiredMixin,generic.DetailView):
  template_name = 'task_app/task_detail.html'
  context_object_name = 'task'


  def get_queryset(self):
    return Task.objects.all()


class TaskCreateView(LoginRequiredMixin,generic.CreateView):
  template_name = 'task_app/task_create.html'
  form_class = TaskModelForm


  def form_valid(self, form):
    task = form.save()
    return super(TaskCreateView, self).form_valid(form)

  def get_success_url(self):
    return reverse('task_app:task_list')


class TaskUpdateView(LoginRequiredMixin,generic.UpdateView):
  template_name = 'task_app/task_update.html'
  form_class = TaskModelForm

  def get_queryset(self):
    return Task.objects.all()


  def get_success_url(self):
    return reverse('task_app:task_list')



class TaskDeleteView(LoginRequiredMixin,generic.DeleteView):
  template_name = 'task_app/task_delete.html'

  def get_queryset(self):
    return Task.objects.all()


  def get_success_url(self):
    return reverse('task_app:task_list')
