
from django.db import models

class AIAgent(models.Model):
    name = models.CharField(max_length=200)
    sample_questions = models.TextField()
    api_key = models.CharField(max_length=500)

    def __str__(self):
        return self.name
