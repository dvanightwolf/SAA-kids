from django.urls import path
from . import views
app_name = "learnwithyourkids"

urlpatterns = [
    path('', views.display, name='LWYK_display'),
    path('search/', views.search, name='search'),

]
