from django.urls import path
from . import views
from account.views import article
app_name = "learnwithyourkids"

urlpatterns = [
    path('', views.show, name='LWYK_display'),
    path('search/', views.search, name='search'),
    path('articles/', article, name="articles"),

]
