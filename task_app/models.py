from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

# Create your models here.

class User(AbstractUser):
  is_employer = models.BooleanField(default=True)
  is_employee = models.BooleanField(default=False)
  description = models.CharField(max_length=200, null=True, blank=True)
  age = models.IntegerField(default=0)
  phone_number = models.CharField(max_length=20, null=True, blank=True)


class UserProfile(models.Model):
  user = models.OneToOneField("User", on_delete=models.CASCADE)
  


  def __str__(self):
    return self.user.username


class Task(models.Model):
  title = models.CharField(max_length=120)
  description = models.TextField(max_length=300)
  employee = models.ForeignKey("Employee", null=True, blank=True, on_delete=models.SET_NULL)
  created_at = models.DateTimeField(auto_now_add=True)
  category = models.ForeignKey("Category", on_delete=models.CASCADE)
  organisation = models.ForeignKey("UserProfile", on_delete=models.CASCADE)
  

  def __str__(self):
    return self.title
  

class Employee(models.Model):
  user = models.OneToOneField("User", on_delete=models.CASCADE)
  organisation = models.ForeignKey("UserProfile", on_delete=models.CASCADE)
  
  def __str__(self):
    return self.user.username

  @property
  def get_email(self):
    return self.user.email


class Category(models.Model):
  name = models.CharField(max_length=60)
  organisation = models.ForeignKey("UserProfile", on_delete=models.CASCADE)

  def __str__(self):
    return self.name


def user_creation_signal(sender, instance, created, **kwargs):
  if created:
    UserProfile.objects.create(user=instance)


post_save.connect(user_creation_signal, sender=User)


