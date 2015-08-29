from django.db import models

class EssayPost(models.Model):
    title = models.CharField(max_length=100)
    essay = models.CharField(max_length=5000)
    time_stamp = models.DateTimeField(auto_now_add=True)