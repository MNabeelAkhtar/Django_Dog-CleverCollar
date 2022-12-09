from datetime import datetime
from email.policy import default
from django.core import validators
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.

class User(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


class Post(models.Model):
    name = models.CharField(max_length=100, null=True, default="Tommy")
    age = models.IntegerField(max_length=5, null=True, default=0)
    breed = models.CharField(max_length=20, null=True, default=None)
    owner_name = models.CharField(max_length=20, default="Shimon")
    owner_number = models.IntegerField(max_length=20, null=True, default="03207051998")
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    date = models.DateField(default=datetime.now)
    excerpt = models.TextField(null=True)
    content = models.TextField(null=True)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='images')
    sec_image = models.ImageField(upload_to='images', default=None)
    mor_image = models.ImageField(upload_to='images', default=None)



    def __str__(self):
        return f"{self.title} | By {self.author}"