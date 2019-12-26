from django.db import models

# Create your models here.
class Sentence(models.Model):
    original_text=models.CharField(max_length=200)
    encoding_text=models.CharField(max_length=200)
    def __str__(self):
        return self.encoding_text

