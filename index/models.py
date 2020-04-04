from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Index(models.Model):
    title= models.CharField(max_length=50)
    content=RichTextField()
