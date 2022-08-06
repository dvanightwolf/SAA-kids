from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager


# Create your models here.
class WorkShops(models.Model):
    title = models.CharField(max_length=256, null=False)
    slug = models.SlugField(max_length=256)
    tags = TaggableManager()
    location = models.CharField(null=True, blank=False, max_length=400)
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=False, blank=False)
    post_photo = models.ImageField(upload_to="workshops/", blank=True, null=False,
                                   default="default_photo.jpg")
    min_required_age = models.IntegerField(null=False, blank=False)
    max_required_age = models.IntegerField(null=False, blank=False)
    form_url = models.URLField(null=False, blank=False)
    description = models.TextField()
    note = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + "_" + str(self.start_date)

    def get_url(self):
        return reverse('workshops:details', args=[self.id, self.slug])


class Day(models.Model):
    workshop = models.ForeignKey(WorkShops, on_delete=models.CASCADE, null=False, blank=False)
    day = models.DateField(null=False, blank=False)
    start_time = models.TimeField(null=False, blank=False)
    end_time = models.TimeField(null=False, blank=False)
    location = models.CharField(max_length=400, null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return str(self.workshop)


class Photo(models.Model):
    workshop = models.ForeignKey(WorkShops, on_delete=models.CASCADE, null=False, blank=False)
    photo = models.ImageField(upload_to="workshops/", blank=True, null=False)

    def __str__(self):
        return str(self.workshop)


class Material(models.Model):
    workshop = models.ForeignKey(WorkShops, on_delete=models.CASCADE, null=False, blank=False)
    google_drive_url = models.URLField(null=False, blank=False)
    youtube_url = models.URLField(null=False, blank=False)

    def __str__(self):
        return str(self.workshop)
