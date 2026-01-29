from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()

    def __str__(self):
        return self.title
