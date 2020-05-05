from django.db import models

# Create your models here.
class Job(models.Model):
    #images
    Image = models.ImageField(upload_to='images/')
    #summary
    Summary = models.CharField(max_length =200)
