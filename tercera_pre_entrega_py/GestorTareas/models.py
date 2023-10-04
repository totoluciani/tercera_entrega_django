from django.db import models

class User(models.Model):

    name = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    email = models.EmailField()

class Task(models.Model):
    name = models.CharField(max_length=40)
    deliverydate = models.DateField()
    status = models.BooleanField()

class TaskDescription(models.Model):
    task = models.OneToOneField(Task, on_delete=models.CASCADE) #Este campo trata al  model como un OneToOnefield que, en terminos simples, hace que el model 'Task' dependa de este campo y viceversa
    description = models.TextField()

    def __str__(self):
        return f"Descripción de la tarea: {self.task.name}"

