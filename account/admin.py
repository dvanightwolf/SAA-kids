from django.contrib import admin
from .models import Profile, MainPageArticle


# Register the profile model to the admin site
@admin.register(Profile)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "email", "bio", "is_staff"]


@admin.register(MainPageArticle)
class MainPageArticleAdmin(admin.ModelAdmin):
    list_display = ["article"]
