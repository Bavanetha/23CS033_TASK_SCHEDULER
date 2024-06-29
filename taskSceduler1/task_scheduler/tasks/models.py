# tasks/models.py


from django.db import models

class Task(models.Model):
    

    name = models.CharField(max_length=100)
    due_date = models.DateTimeField()
    
    user_type = models.CharField(max_length=10, choices=[('worker', 'Worker'), ('tester', 'Tester')])
    is_completed = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
# models.py





