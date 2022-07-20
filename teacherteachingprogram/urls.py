from django.urls import path
from . import views
app_name = "teacherteachingprogram"

urlpatterns = [
    path('', views.display, name='ttp_display'),
    path('search/',views.search,name='search_ttp'),
    path('<int:ttp_id>/<slug:ttp_slug>/', views.ttp_details, name='ttp_details'),
    path('<int:ttp_id>/', views.check, name='check_code')

]
