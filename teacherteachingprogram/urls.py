from django.urls import path
from . import views
app_name = "teacherteachingprogram"

urlpatterns = [
    path('', views.display, name='ttp_display'),
    path('search/', views.search, name='search_ttp'),
    path('<int:ttp_id>/<slug:ttp_slug>/', views.ttp_details, name='ttp_details'),
    path('<int:ttp_id>/<slug:ttp_slug>/', views.ttp_details, name='check_code'),
    path('ttp-article/', views.ttp_article, name='ttp_article'),
    path('ttp-article/<article_id>/<slug:slug>/', views.ttp_article_details, name='ttp_article_details'),

]
