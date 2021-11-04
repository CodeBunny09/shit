from datetime import date, datetime, timezone
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.fields.related_descriptors import create_forward_many_to_many_manager
from django.utils.text import slugify


import datetime

# Create your models here.

class HomePageData(models.Model):
    intro = RichTextUploadingField(max_length=10000, null=True, blank=True)
    about = RichTextUploadingField(max_length=10000, null=True, blank=True)

    #Social Links
    twitter = models.URLField(max_length=100, null=True, blank=True)
    facebook = models.URLField(max_length=100, null=True, blank=True)
    instagram = models.URLField(max_length=100, null=True, blank=True)
    github = models.URLField(max_length=100, null=True, blank=True)

    def __str__(self):
        return "HomePageData"

class Catagory(models.Model):
    thumbnail = models.ImageField(null=True, blank=True, upload_to='images/cat', default='/static/images/pic02.jpg')
    name = models.CharField(max_length=200, blank=True, unique=True)

    class Meta:
        verbose_name_plural = "Catagories"

    def __str__(self):
        return self.name
    

class Comment(models.Model):
    content = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:20]

class Post(models.Model):
    thumbnail = models.ImageField(null=True, blank=True, upload_to='images/posts', default='/static/images/pic02.jpg')
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=400)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    content = RichTextUploadingField(max_length=10000, null=True, blank=True)
    catagory = models.ManyToManyField(Catagory, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    private = models.BooleanField(default=True)
    comments = models.ManyToManyField(Comment, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.title}{datetime.date.today()}{timezone.now()}')
        super(Post, self).save(*args, **kwargs)

    # @property
    # def url(self):
    #     return reverse()

    def __str__(self):
        return self.title