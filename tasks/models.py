from django.db import models

class Task(models.Model):
    taskname=models.TextField(max_length=250)
    completed=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.taskname