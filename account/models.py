from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.urls import reverse


class Profile(AbstractUser):
    # Holds the user's bio
    bio = models.CharField(max_length=300, blank=True, null=True)


class Article(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    slug = models.SlugField(max_length=255, null=False, blank=False)
    first_article = models.TextField()
    first_photo = models.ImageField(upload_to="article/", blank=True, null=False)
    last_article = models.TextField()
    last_photo = models.ImageField(upload_to="article/", blank=True, null=False)
    video_url = models.URLField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('article_details', args=[self.pk, self.slug])

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=False)
    comment = models.TextField(null=False, blank=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.article.title + "__" + self.comment
