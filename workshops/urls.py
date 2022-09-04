from django.urls import path
from . import views
app_name = "workshops"

urlpatterns = [
    path('', views.workshops_activities, name="workshops_activities"),
    path('<workshop_id>/<slug:slug>', views.details, name="details"),
    path('serach/', views.search, name='search'),
    path('archive/', views.archive, name='archive'),

]
