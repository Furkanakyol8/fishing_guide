from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.utils.html import strip_tags

class Category(models.Model):
    name=models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True, unique=True, db_index=True, editable=False)

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)



class Fishes(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to="fishes/")
    description = RichTextField()
    summarizedDescription = models.CharField(null=True, blank=True, max_length=70)
    tactic = RichTextField(null=True)
    slug = models.SlugField(null=False, unique=True, blank=True, db_index=True, editable=False)
    category = models.ForeignKey(Category, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.summarizedDescription = strip_tags(self.description)[:70];
        super().save(*args, **kwargs)
