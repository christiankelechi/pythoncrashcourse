from django.db import models

# Create your models here.
class Fruit(models.Model):
    name=models.CharField(max_length=200,help_text='name of fruit')
    color=models.CharField(max_length=200,help_text='color of the fruit')
    description=models.TextField()
