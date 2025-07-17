from django.db import models

class Word(models.Model):
    english = models.CharField(max_length=100)
    polish = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.english} - {self.polish}"