from django.db import models


class ToDo(models.Model):
    todo = models.CharField(max_length=200)
    started_on = models.DateField()
    due_on = models.DateField()
    owner = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.todo
