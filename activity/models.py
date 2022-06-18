from django.db import models


# Create your models here.
class Activity(models.Model):
    title = models.CharField(max_length=255, null=False)
    photo = models.ImageField(upload_to="activity/", blank=True, null=False,
                              default="activity/default_activity_photo.jpg")
    date = models.DateField(null=False, blank=False)
    start_time = models.TimeField(null=False, blank=False)
    end_time = models.TimeField(null=False, blank=False)
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


class ActivityPhoto(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, null=False)
    photo = models.ImageField(upload_to="activity/", blank=True, null=False,
                              default="activity/default_activity_photo.jpg")

    def __str__(self):
        return self.activity


