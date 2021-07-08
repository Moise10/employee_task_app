from django.contrib import admin
from .models import Task, User, Employee, UserProfile, Category
# Register your models here.

admin.site.register(Task)
admin.site.register(Employee)
admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Category)
