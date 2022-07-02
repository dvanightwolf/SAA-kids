from django.contrib import admin
from .models import WorkShops, Day, Photo, Material
# Register the profile model to the admin site


class DayAdmin(admin.StackedInline):
    model = Day


class PhotoAdmin(admin.StackedInline):
    model = Photo


class MaterialAdmin(admin.StackedInline):
    model = Material


@admin.register(WorkShops)
class WorkShopsAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description", "note", "start_date", "end_date", "location", "min_required_age",
                    "max_required_age", "form_url", "is_active", "created", "updated", ]
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ("title", "start_date")
    ordering = ("-created",)
    inlines = [DayAdmin, MaterialAdmin, PhotoAdmin]



