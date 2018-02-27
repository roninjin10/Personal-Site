from django.db import models

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=140)
  body = models.TextField()
  html = models.TextField(default='no html here')
  date = models.DateTimeField()

  def __str__(self):
    return self.title