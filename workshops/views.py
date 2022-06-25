from django.shortcuts import render, get_object_or_404
from .models import WorkShops, Day, Photo, Material


def show(request):
    """List all workshops."""
    # Get all workshops.
    workshops = WorkShops.objects.all().order_by('-id')
    days = Day.objects.all().order_by('day')
    # Put the info in a dictionary.
    context = {"workshops": workshops, "days": days}
    # Render show page and send the dictionary to it.
    return render(request, "workshops_show.html", context)


def details(request, workshop_id, slug):
    """Show workshop details."""
    # Get workshop by id.
    workshop = get_object_or_404(WorkShops, pk=workshop_id, slug=slug)
    days = Day.objects.filter(workshop=workshop)
    photos = Photo.objects.filter(workshop=workshop)
    materials = Material.objects.filter(workshop=workshop)
    # Put the info in a dictionary.
    context = {"workshop": workshop, "days": days, "photos": photos, "materials": materials}
    # Render details page and send the dictionary to it.
    return render(request, "workshops_details.html", context)