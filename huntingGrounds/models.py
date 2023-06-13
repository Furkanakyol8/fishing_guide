from django.db import models
from fishes.models import Fishes
from ckeditor.fields import RichTextField

class Grounds(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True, upload_to="grounds/")
    description = models.TextField()
    summarizedDescription = models.CharField(null=True, blank=True, max_length=99999)
    fishes = models.ManyToManyField(Fishes)
    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        self.summarizedDescription = self.description[:99999];
        super().save(*args, **kwargs)
