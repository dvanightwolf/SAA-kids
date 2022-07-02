from django.urls import path
from . import views
app_name = "activity"

urlpatterns = [
    path('<int:activity_id>/<slug:activity_slug>/', views.act_details, name='activity_details'),

]
