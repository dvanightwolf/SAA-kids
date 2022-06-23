from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager


class Activity(models.Model):
    title = models.CharField(max_length=256, null=False)
    slug = models.SlugField(max_length=256)
    tags = TaggableManager()
    date = models.DateField(null=False, blank=False)
    start_time = models.TimeField(null=False, blank=False)
    end_time = models.TimeField(null=False, blank=False)
    post_photo = models.ImageField(upload_to="activity/", blank=True, null=False,
                                   default="default_photo.jpg")
    location = models.CharField(null=False, blank=False, max_length=400)
    min_required_age = models.IntegerField(null=False, blank=False)
    max_required_age = models.IntegerField(null=False, blank=False)
    form_url = models.URLField(null=False, blank=False)
    description = models.TextField()
    note = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + str(self.date)

    def get_url(self):
        return reverse('activity:activity_details', args=[self.id, self.slug])


class ActivityPhoto(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, null=False)
    photo = models.ImageField(upload_to="activity/", blank=True, null=False)

    def __str__(self):
        return str(self.activity)


