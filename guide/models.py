from django.db import models
from ckeditor.fields import RichTextField
from django.utils.html import strip_tags
from django.utils.text import slugify


class Guide(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True, upload_to="guides/")
    description = RichTextField()
    summarizedDescription = models.CharField(null=True, blank=True, max_length=30)
    slug = models.SlugField(null=True, blank=True, unique=True, db_index=True, editable=False)

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.summarizedDescription = strip_tags(self.description)[:30];
        super().save(*args, **kwargs)