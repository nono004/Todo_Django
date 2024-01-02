from django.db import models
import datetime

# Create your models here.
class TodoModel(models.Model):
    Todo = models.TextField()
    DeadLine = models.DateField(default=datetime.date.today)
    Category_Choices = (
        ('work', '仕事'),
        ('study', '勉強'),
        ('hobby', '趣味'),
        ('others', 'その他'),
    )
    Category = models.CharField(max_length=10, choices=Category_Choices, blank=True)

