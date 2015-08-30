from django.db import models

class EssayPost(models.Model):
    title = models.CharField(max_length=100)
    essay = models.TextField()
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
