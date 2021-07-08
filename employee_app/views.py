import random
from django.shortcuts import render, reverse
from django.views import generic
from django.core.mail import send_mail
from task_app.models import Employee , Task
from .forms import EmployeeModelForm
from .mixins import LoginAndEmployeeRequiredMixin


class EmployeeListView(LoginAndEmployeeRequiredMixin,generic.ListView):
  template_name = 'employee_app/employee_list.html'
  context_object_name = 'employees'

  def get_queryset(self):
    queryset = Employee.objects.filter(
      organisation = self.request.user.userprofile
    )
    return queryset


class EmployeeDetailView(LoginAndEmployeeRequiredMixin,generic.DetailView):
  template_name = 'employee_app/employee_detail.html'
  context_object_name = 'employee'

  def get_queryset(self):
    queryset = Employee.objects.filter(
        organisation=self.request.user.userprofile
    )
    return queryset


class EmployeeCreateView(LoginAndEmployeeRequiredMixin, generic.CreateView):
  template_name = 'employee_app/employee_create.html'
  form_class = EmployeeModelForm

  def get_success_url(self):
    return reverse('employee_app:employee_list')

  def form_valid(self, form):
    user = form.save(commit=False)
    user.is_employer = False
    user.is_employee = True
    user.set_password(f"{random.randint(0,10000)}")
    form.save()
    Employee.objects.create(
      user=user,
      organisation = self.request.user.userprofile
    )
    send_mail(
      subject="You have been set as an agent into STANBYCRM please come and login!",
      from_email="moise@gmail.com",
      message="Login and start working as soon as possible!",
      recipient_list=['paul_smith@yahoo.com'],
    )
    return super(EmployeeCreateView, self).form_valid(form)


class EmployeeUpdateView(LoginAndEmployeeRequiredMixin, generic.UpdateView):
  template_name = 'employee_app/employee_update.html'
  form_class = EmployeeModelForm

  def get_queryset(self):
    return Employee.objects.all()

  def get_success_url(self):
    return reverse('employee_app:employee_list')


class EmployeeDeleteView(LoginAndEmployeeRequiredMixin, generic.DeleteView):
  template_name = 'employee_app/employee_delete.html'
  
  def get_queryset(self):
    queryset = Employee.objects.filter(
        organisation=self.request.user.userprofile
    )
    return queryset

  def get_success_url(self):
    return reverse('employee_app:employee_list')



