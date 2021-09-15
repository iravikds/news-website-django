from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)