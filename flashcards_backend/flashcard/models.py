from django.db import models


# Create your models here.

class Flashcard(models.Model):
    flashcard_title = models.CharField(max_length=50)
    flashcard_word = models.CharField(max_length=50)
    flashcard_definition = models.CharField(max_length=50)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, default=None, null=True)
