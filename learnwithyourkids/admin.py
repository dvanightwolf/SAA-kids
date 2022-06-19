from django.contrib import admin
from .models import LearnWithYourKids


# Register your models here.
@admin.register(LearnWithYourKids)
class LearnWithYourKidsAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "url", "photo"]
    search_fields = ("title",)
    ordering = ("title",)
    add_form_template = "talon.html"
