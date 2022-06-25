from django.urls import path
from . import views
app_name = "learnwithyourkids"

urlpatterns = [
    path('', views.show, name='LWYK_display'),
    path('search/', views.search, name='search'),

]
