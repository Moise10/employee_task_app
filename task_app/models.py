from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

# Create your models here.

class User(AbstractUser):
  is_employer = models.BooleanField(default=True)
  is_employee = models.BooleanField(default=False)

class UserProfile(models.Model):
  user = models.OneToOneField("User", on_delete=models.CASCADE)


  def __str__(self):
    return self.user.username


class Task(models.Model):
  title = models.CharField(max_length=120)
  description = models.TextField(max_length=300)
  employee = models.ForeignKey("Employee", null=True, blank=True, on_delete=models.SET_NULL)
  created_at = models.DateTimeField(auto_now_add=True)
  organisation = models.ForeignKey("UserProfile", on_delete=models.CASCADE)
  

  def __str__(self):
    return self.title


class Employee(models.Model):
  user = models.OneToOneField("User", on_delete=models.CASCADE)
  organisation = models.ForeignKey("UserProfile", on_delete=models.CASCADE)
  

  def __str__(self):
    return self.user.email


def user_creation_signal(sender, instance, created, **kwargs):
  if created:
    UserProfile.objects.create(user=instance)


post_save.connect(user_creation_signal, sender=User)

