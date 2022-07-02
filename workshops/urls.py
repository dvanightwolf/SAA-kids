from django.urls import path
from . import views
app_name = "workshops"

urlpatterns = [
    path('', views.show, name="show"),
    path('<workshop_id>/<slug:slug>', views.details, name="details"),
    path('serach/', views.search, name='search'),
    path('archive/', views.archive, name='archive')

]
