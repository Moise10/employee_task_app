from django.shortcuts import render, reverse
from django.views import generic
from task_app.models import Employee , Task
from .forms import EmployeeModelForm


class EmployeeListView(generic.ListView):
  template_name = 'employee_app/employee_list.html'
  context_object_name = 'employees'

  def get_queryset(self):
    return Employee.objects.all()


class EmployeeDetailView(generic.DetailView):
  template_name = 'employee_app/employee_detail.html'
  context_object_name = 'employee'

  def get_queryset(self):
    return Employee.objects.all()


class EmployeeCreateView(generic.CreateView):
  template_name = 'employee_app/employee_create.html'
  form_class = EmployeeModelForm

  def get_success_url(self):
    return reverse('employee_app:employee_list')

  def form_valid(self, form):
    user = form.save(commit=False)
    user.is_employer = False
    user.is_employee = True
    form.save()
    Employee.objects.create(
      user=user,
      organisation = self.request.user.userprofile
    )
    return super(EmployeeCreateView, self).form_valid(form)



class EmployeeUpdateView(generic.UpdateView):
  template_name = 'employee_app/employee_update.html'
  form_class = EmployeeModelForm

  def get_queryset(self):
    return Employee.objects.all()

  def get_success_url(self):
    return reverse('employee_app:employee_list')


class EmployeeDeleteView(generic.DeleteView):
  template_name = 'employee_app/employee_delete.html'
  
  def get_queryset(self):
    return Employee.objects.all()

  def get_success_url(self):
    return reverse('employee_app:employee_list')



