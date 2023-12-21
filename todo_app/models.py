from django.db import models
import datetime

# Create your models here.
class TodoModel(models.Model):
    Todo = models.TextField()
    DeadLine = models.DateField(default=datetime.date.today)