from django.db import models
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    title= models.CharField(max_length=100)
    author= models.CharField(max_length=50)
    datetime= models.DateTimeField(default=timezone.now)
    description=models.TextField()
    code=models.TextField()
    conclusion=models.TextField()

    def __str__(self):
        return f"{self.title}  |  {self.author}"

    def get_absolute_url(self):
        return reverse("projects")