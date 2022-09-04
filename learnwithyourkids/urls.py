from django.urls import path
from . import views
from account.views import article, article_search
app_name = "learnwithyourkids"

urlpatterns = [
    path('', views.show, name='LWYK_display'),
    path('search/', views.search, name='search'),
    path('articles/', article, name="articles"),
    path('article-search/', article_search, name='article_search')

]
