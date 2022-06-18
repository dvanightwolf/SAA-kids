from django.contrib import admin
from .models import WorkShops, Day, Photo, Material
# Register the profile model to the admin site


@admin.register(WorkShops)
class WorkShopsAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description", "note", "start_date", "end_date", "location", "min_required_age",
                    "max_required_age", "form_url", "is_active", "created", "updated", ]
    search_fields = ("title", "start_date")
    ordering = ("-created",)


@admin.register(Day)
class DayAdmin(admin.ModelAdmin):
    list_display = ["workshop", "day", "start_time", "end_time", "location", "description", ]
    ordering = ("workshop",)


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ["workshop", "photo"]
    ordering = ("workshop",)


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ["workshop", "google_drive_url", "youtube_url"]
    ordering = ("workshop",)
