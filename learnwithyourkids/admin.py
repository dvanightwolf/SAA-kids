from django.contrib import admin
from .models import LearnWithYourKids


# Register your models here.
@admin.register(LearnWithYourKids)
class LearnWithYourKidsAdmin(admin.ModelAdmin):
    list_display = ["title", "description", 'tags', "url", "photo"]
    search_fields = ("title",)
    ordering = ("title",)

