from django.contrib import admin
from .models import *

@admin.register(TTP)
class TeacherTeachingAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description", "start_date", "end_date", "location",
                    "form_url", "is_active", "created", "updated"]
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ("title", "start_date")
    ordering = ("-created",)


@admin.register(Day)
class DayAdmin(admin.ModelAdmin):
    list_display = ["ttp", "day", "start_time", "end_time", "location", "description", ]
    ordering = ("ttp",)


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ["ttp", "photo"]
    ordering = ("ttp",)


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ["ttp", "google_drive_url", "youtube_url"]
    ordering = ("-ttp",)
