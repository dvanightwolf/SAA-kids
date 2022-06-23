from django.urls import path
from . import views
app_name = "teacherteachingprogram"

urlpatterns = [
    path('', views.display, name='ttp_display'),
    path('<int:ttp_id>/<slug:ttp_slug>/', views.ttp_details, name='ttp_details')

]
