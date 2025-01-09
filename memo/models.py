from django.db import models
from django.urls import reverse

# Create your models here.


class Memo(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("top")
