from django.urls import path
from . import views
app_name = "learnwithyourkids"

urlpatterns = [
    path('', views.show, name="show"),
    path('details/<learn_id>/', views.details, name="details"),

]
