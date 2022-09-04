"""SAA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from account.views import base, no_page_found, article_details, contact
from django.conf.urls import handler404, handler403, handler500, handler400

urlpatterns = [
    path('', base, name="home"),
    path('article-details/<article_id>/<slug:slug>/', article_details, name="article_details"),
    path('admin/', admin.site.urls),
    path('contact/', contact, name='contact'),
    path('workshops-and-activities/', include('workshops.urls')),
    path('learn-with-your-kids/', include('learnwithyourkids.urls')),
    path('TTP/', include('teacherteachingprogram.urls')),
    path('activities/', include('activity.urls')),
    path('games/', include('games.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.AST_URL, document_root=settings.AST_FILES)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = no_page_found
handler403 = no_page_found
handler400 = no_page_found
#handler500 = no_page_found
