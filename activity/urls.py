from django.urls import path
from . import views
app_name = "activity"

urlpatterns = [
    path('', views.display, name='activity_display'),
    path('<int:activity_id>/<slug:activity_slug>/', views.act_details, name='activity_details'),
    path('search/', views.search, name='search'),

]
