from django.db import models

# Create your models here.


class NoteEntity(models.Model):
  title = models.CharField(max_length=100)
  noteText = models.CharField(max_length=10000)