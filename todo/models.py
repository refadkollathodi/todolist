from django.db import models


class todo(models.Model):
    task=models.TextField(max_length=255)
    
    def __str__(self):
        return self.task
