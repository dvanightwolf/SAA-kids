from django.contrib import admin
from .models import Activity, ActivityPhoto


# Register the profile model to the admin site


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description", 'tags', "note", "date", "start_time", "end_time", "min_required_age",
                    "max_required_age", "form_url", "is_active", "created", "updated"]
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ("title", "date")
    ordering = ("-date",)



@admin.register(ActivityPhoto)
class ActivityPhotoAdmin(admin.ModelAdmin):
    list_display = ["activity", "photo"]
    ordering = ("activity",)
