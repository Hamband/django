from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class BlogPost(models.Model):
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True),
    poster = models.CharField(max_length=300, null=True, blank=True)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.subject)
        super(BlogPost, self).save(*args, **kwargs)
