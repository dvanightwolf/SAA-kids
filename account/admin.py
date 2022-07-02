from django.contrib import admin
from .models import Profile, Article, Comment, ArticleContent


# Register the profile model to the admin site
@admin.register(Profile)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "email", "bio", "is_staff"]


class ArticleContentAdmin(admin.StackedInline):
    model = ArticleContent


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "video_url"]
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ArticleContentAdmin]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["article", "name", "comment"]
