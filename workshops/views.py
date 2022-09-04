from django.shortcuts import render, get_object_or_404
from activity.models import Activity, ActivityPhoto
from .models import WorkShops, Day, Photo, Material
from taggit.models import Tag
from django.db.models import Q


def search(request):
    workshops = []
    activities = []
    tags = Tag.objects.all()
    photos = Photo.objects.all()
    activity_photo = ActivityPhoto.objects.all()
    tag = Tag()
    query = None
    if request.method == 'GET':
        start_date = request.GET.get('SDate')
        end_date = request.GET.get('EDate')
        query = request.GET.get('search')
        tag_id = request.GET.get('tag', 'None')
        if tag:
            tag = Tag.objects.filter(pk=tag_id)
        if query != '':
            if WorkShops.objects.filter(Q(tags__name=query)):
                workshops = WorkShops.objects.filter(Q(tags__name=query))
            else:
                workshops = WorkShops.objects.filter(Q(title__icontains=query) |
                                                     Q(description__icontains=query))
        elif query == '' or tag == "0":
            workshops = WorkShops.objects.all()

        if tag_id != '0':
            workshops = workshops.filter(Q(tags__name=tag[0].name))
        if end_date and start_date:
            workshops = workshops.filter(start_date__range=[start_date, end_date])
        elif start_date:
            workshops = workshops.filter(start_date=start_date)

        if query != '':
            if Activity.objects.filter(Q(tags__name=query)):
                activities = Activity.objects.filter(Q(tags__name=query))
            else:
                activities = Activity.objects.filter(Q(title__icontains=query) |
                                                     Q(description__icontains=query))
        elif query == '' or tag == "0":
            activities = Activity.objects.all()

        if tag_id != '0':
            activities = activities.filter(Q(tags__name=tag[0].name))
        if end_date and start_date:
            activities = activities.filter(date__range=[start_date, end_date])
        elif start_date:
            activities = activities.filter(date=start_date)

    return render(request, 'workshops_and_activities_show.html', {'workshops': workshops,
                                                                  'activity': activities})


def workshops_activities(request):
    # Get all workshops.
    workshops = WorkShops.objects.filter(is_active=True).order_by('-id')
    # Get all activities.
    activity = Activity.objects.filter(is_active=True).order_by('-id')
    # Put the info in a dictionary.
    context = {"workshops": workshops,
               "activity": activity}
    # Render show page and send the dictionary to it.
    return render(request, "workshops_and_activities_show.html", context)


def details(request, workshop_id, slug):
    """Show activity details."""
    # Get activity by id.
    workshop = get_object_or_404(WorkShops, pk=workshop_id, slug=slug)
    days = Day.objects.filter(workshop=workshop)
    photos = Photo.objects.filter(workshop=workshop)
    materials = Material.objects.filter(workshop=workshop)
    # Put the info in a dictionary.
    context = {"workshop": workshop, "days": days, "photos": photos, "materials": materials}
    # Render details page and send the dictionary to it.
    return render(request, "workshops_details.html", context)


def archive(request):
    # Get all workshops.
    workshops = WorkShops.objects.filter(is_active=False).order_by('-id')
    # Get all activities.
    activity = Activity.objects.filter(is_active=False).order_by('-id')
    # Put the info in a dictionary.
    context = {"workshops": workshops,
               "activity": activity}
    # Render show page and send the dictionary to it.
    return render(request, "workshops_and_activities_show.html", context)
