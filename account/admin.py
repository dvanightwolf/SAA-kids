from django.contrib import admin
from .models import Profile, Article, Comment


# Register the profile model to the admin site
@admin.register(Profile)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "email", "bio", "is_staff"]


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "first_article", "video_url"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["article", "comment"]
