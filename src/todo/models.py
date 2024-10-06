from django.db import models

# Create your models here.

class TodoItem(models.Model):
    """ A TodoItem. """
    name = models.CharField(max_length=80, unique=True)
    description = models.TextField()
    due_date = models.DateTimeField(blank=True, null=True)
    done = models.BooleanField(default=False)
