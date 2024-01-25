from django.db import models

# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length = 20)
    date = models.DateField()
    priority = models.CharField(max_length = 20)

    def __str__(self):
        return f"Task is {self.task}, Date to complete the task is {self.date}, Priority to the task is {self.priority}"
    

class Login(models.Model):
    email = models.EmailField()
    password  = models.CharField(max_length=128)

    def __str__(self):
        return f"Email is {self.email}, password is {self.password}"