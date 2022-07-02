from django.shortcuts import render, get_object_or_404
from .models import Activity, ActivityPhoto


def act_details(request, activity_id, activity_slug):
    activity = get_object_or_404(Activity, pk=activity_id, slug=activity_slug)
    photos = ActivityPhoto.objects.filter(activity_id=activity)
    context = {"activity": activity, "photos": photos}
    return render(request, "activity_details.html", context)

