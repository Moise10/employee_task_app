from django import forms
from .models import Task, Employee


class TaskModelForm(forms.ModelForm):
  class Meta:
    model = Task
    fields = ('title', 'employee', 'description',)
    


class EmployeeAssignForm(forms.Form):
  employee = forms.ModelChoiceField(queryset=Employee.objects.none())

  def __init__(self, *args, **kwargs):
    request = kwargs.pop('request')
    employees = Employee.objects.filter(organisation=request.user.userprofile)
    super(EmployeeAssignForm, self).__init__(*args, **kwargs)
    self.fields['employee'].queryset = employees

