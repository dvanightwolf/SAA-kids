from django.db import models
from django.urls import reverse


class LearnWithYourKids(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(null=False, blank=False)
    url = models.URLField(null=False, blank=False)
    photo = models.ImageField(upload_to="learnwithyourkids/", blank=True, null=False,
                              default="learnwithyourkids/default_learnwithyourkids_photo.jpg")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def detail_url(self):
        return reverse("learnwithyourkids:details", args=[self.pk])

    def __str__(self):
        return self.title
