from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class EmployeeModelForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ('first_name', 'last_name', 'email',
              'username', 'description', 'phone_number')
