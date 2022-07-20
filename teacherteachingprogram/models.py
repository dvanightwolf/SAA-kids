from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager


class TTP(models.Model):
    title = models.CharField(max_length=256, null=False, blank=False)
    slug = models.SlugField(max_length=256)
    tags = TaggableManager()
    post_photo = models.ImageField(upload_to="TTP/", blank=False, null=False,
                              default="TTP/default_TTP_photo.jpg")
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=False, blank=False)
    teaching_grade = models.CharField(max_length=100)
    description = models.TextField()
    form_url = models.URLField(null=False, blank=False)
    location = models.CharField(null=False, blank=False, max_length=400)
    material_password = models.CharField(max_length=50, null=True, blank=True)
    lock = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title + str(self.created)

    def get_url(self):
        return reverse('teacherteachingprogram:ttp_details', args=[self.id, self.slug])

    def check_id(self):
        return reverse('teacherteachingprogram:check_code', args=[self.id])


class Day(models.Model):
    ttp = models.ForeignKey(TTP, on_delete=models.CASCADE, null=False, blank=False)
    day = models.DateField(null=False, blank=False)
    start_time = models.TimeField(null=False, blank=False)
    end_time = models.TimeField(null=False, blank=False)
    location = models.CharField(max_length=400, null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return str(self.ttp)


class Photo(models.Model):
    ttp = models.ForeignKey(TTP, on_delete=models.CASCADE, null=False, blank=False)
    photo = models.ImageField(upload_to="TTP/", blank=True, null=False)

    def __str__(self):
        return str(self.ttp)


class Material(models.Model):
    ttp = models.ForeignKey(TTP, on_delete=models.CASCADE, null=False, blank=False)
    google_drive_url = models.URLField(null=False, blank=False)
    youtube_url = models.URLField(null=False, blank=False)

    def __str__(self):
        return str(self.ttp)
