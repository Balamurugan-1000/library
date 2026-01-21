from django.db import models

# Create your models here.

class Book(models.Model):
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    total_copies=models.PositiveBigIntegerField()

    def __str__(self):
        return str(self.title)
