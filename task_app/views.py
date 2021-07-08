from django.db.models import Count
from django.shortcuts import render, reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from .models import Task , Category
from .forms import TaskModelForm, EmployeeAssignForm
from employee_app.mixins import LoginAndEmployeeRequiredMixin


def get_category_count():
  queryset = Task.objects.values('category__name').annotate(Count("category__name"))
  return queryset



class LandingPageView(generic.TemplateView):
  template_name = 'landing_page.html'


class TaskListView(LoginRequiredMixin,generic.ListView):
  template_name = 'task_app/task_list.html'
  context_object_name = 'tasks'

  def get_queryset(self):
    user = self.request.user
    organisation = user.userprofile
    if user.is_employer:
      queryset = Task.objects.filter(organisation=organisation, employee__isnull=False).order_by('-created_at')
    else:
      queryset = Task.objects.filter(
          organisation=user.employee.organisation, employee__isnull=False)
      queryset = queryset.filter(employee__user=user)
    return queryset

  def get_context_data(self, **kwargs):
    context = super(TaskListView, self).get_context_data(**kwargs)
    user = self.request.user
    if user.is_employer:
      queryset = Task.objects.filter(organisation=user.userprofile,employee__isnull=True)
    else:
      queryset = Task.objects.filter(
          organisation=user.employee.organisation, employee__isnull=True)
      queryset = queryset.filter(employee__user=user, employee__isnull=True)
    context.update({
      "unassigned_employees":queryset
    })
    return context




class TaskDetailView(LoginRequiredMixin,generic.DetailView):
  template_name = 'task_app/task_detail.html'
  context_object_name = 'task'

  def get_queryset(self):
    user = self.request.user
    organisation = user.userprofile
    if user.is_employer:
      queryset = Task.objects.filter(organisation=organisation)
    else:
      queryset = Task.objects.filter(organisation=user.employee.organisation)
    return queryset


class TaskCreateView(LoginAndEmployeeRequiredMixin, generic.CreateView):
  template_name = 'task_app/task_create.html'
  form_class = TaskModelForm
  
  def form_valid(self, form):
    task = form.save(commit=False)
    task.organisation = self.request.user.userprofile
    form.save()
    return super(TaskCreateView, self).form_valid(form)

  def get_success_url(self):
    return reverse('task_app:task_list')


class TaskUpdateView(LoginRequiredMixin,generic.UpdateView):
  template_name = 'task_app/task_update.html'
  form_class = TaskModelForm

  def get_queryset(self):
    user = self.request.user
    organisation = user.userprofile
    if user.is_employer:
      queryset = Task.objects.filter(organisation=organisation)
    else:
      queryset = Task.objects.filter(organisation=user.employee.organisation)
    return queryset

  def get_success_url(self):
    return reverse('task_app:task_list')


class TaskDeleteView(LoginAndEmployeeRequiredMixin, generic.DeleteView):
  template_name = 'task_app/task_delete.html'

  def get_queryset(self):
    user = self.request.user
    organisation = user.userprofile
    if user.is_employer:
      queryset = Task.objects.filter(organisation=organisation)
    else:
      queryset = Task.objects.filter(organisation=user.employee.organisation)
    return queryset

  def get_success_url(self):
    return reverse('task_app:task_list')


class AssignEmployee(generic.FormView):
  template_name = 'task_app/assign_employee.html'
  form_class = EmployeeAssignForm

  def get_form_kwargs(self, **kwargs):
    kwargs = super(AssignEmployee, self).get_form_kwargs(**kwargs)
    kwargs.update({
      "request": self.request
    })
    return kwargs
  
  def form_valid(self, form):
    employee = form.cleaned_data["employee"]
    task = Task.objects.get(id=self.kwargs['pk'])
    task.employee = employee
    task.save()
    return super(AssignEmployee, self).form_valid(form)

  def get_success_url(self):
    return reverse('task_app:task_list')


class TaskCategoryView(LoginRequiredMixin,generic.ListView):
  template_name = 'task_app/task_category.html'
  context_object_name = 'categories'

  def get_queryset(self):
    user = self.request.user
    organisation = user.userprofile
    if user.is_employer:
      queryset = Category.objects.filter(organisation=organisation)
    else:
      queryset = Category.objects.filter(
          organisation=user.employee.organisation)
    return queryset

  def get_context_data(self, **kwargs):
    context = super(TaskCategoryView, self).get_context_data(**kwargs)
    user = self.request.user
    if user.is_employer:
      queryset = Task.objects.filter(
          organisation=user.userprofile, employee__isnull=True)
    else:
      queryset = Task.objects.filter(
          organisation=user.employee.organisation, employee__isnull=True)
      queryset = queryset.filter(employee__user=user, employee__isnull=True)
    count_category = Task.objects.filter(category__isnull=True).count()
    get_count = get_category_count
    context.update({
        "unassigned_category_count": count_category,
        "get_category_count": get_count
    })
    return context


class TaskCategoryDetail(generic.DetailView):
  template_name = 'task_app/task_category_detail.html'
  context_object_name = 'category'

  def get_queryset(self):
    user = self.request.user
    organisation = user.userprofile
    if user.is_employer:
      queryset = Category.objects.filter(organisation=organisation)
    else:
      queryset = Category.objects.filter(organisation=user.employee.organisation)
    return queryset
