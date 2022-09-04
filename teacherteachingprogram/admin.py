from django.contrib import admin
from .models import *


class DayAdmin(admin.StackedInline):
    model = Day


class PhotoAdmin(admin.StackedInline):
    model = Photo


class MaterialAdmin(admin.StackedInline):
    model = Material


@admin.register(TTP)
class TeacherTeachingAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description", "start_date", "end_date", "location",
                    "form_url", "is_active", "created", "updated"]
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ("title", "start_date")
    ordering = ("-created",)
    inlines = [DayAdmin, MaterialAdmin, PhotoAdmin]


class TTPArticleContentAdmin(admin.StackedInline):
    model = TTPArticleContent


@admin.register(TTPArticle)
class TTPArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "video_url"]
    prepopulated_fields = {'slug': ('title',)}
    inlines = [TTPArticleContentAdmin]



