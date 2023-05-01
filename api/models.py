from django.db import models

# Create your models here.
class Event(models.Model):
    event_name=models.CharField(max_length=100)
    data=models.TextField(max_length=400)
    time=models.DateField()
    location=models.CharField(max_length=100)
    image=models.ImageField(upload_to="frontend/public/")
    is_liked=models.BooleanField(default=False)

    def __str__(self):
        return self.data[0:50]