from django.db import models
from taggit.managers import TaggableManager


# Create your models here.
class LearnWithYourKids(models.Model):
    title = models.CharField(max_length=256, blank=False, null=False)
    tags = TaggableManager()
    description = models.TextField(null=False, blank=False)
    url = models.URLField(null=False, blank=False)
    photo = models.ImageField(upload_to="learnwithyourkids/", blank=True, null=False,
                              default="learnwithyourkids/default_learnwithyourkids_photo.jpg")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


