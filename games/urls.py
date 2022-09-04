from django.urls import path
from .views import *


app_name = "games"

urlpatterns = [
    path('',api,name='api'),
    path('<int:id>/<str:title>/',play_game,name='play_game'),
    path('solar-system/', solar, name='solar')

]