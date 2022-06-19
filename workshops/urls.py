from django.urls import path
from . import views
app_name = "workshops"

urlpatterns = [
    path('', views.show, name="show"),

]
