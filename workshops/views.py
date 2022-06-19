from django.shortcuts import render
from .models import WorkShops, Day, Photo, Material


def show(request):
    """List all workshops."""
    # Get all workshops.
    workshops = WorkShops.objects.all()
    days = Day.objects.all()
    photos = Photo.objects.all()
    material = Material.objects.all()
    # Put the info in a dictionary.
    context = {"workshops": workshops, "days": days, "photos": photos, "material": material}
    # Render show page and send the dictionary to it.
    return render(request, "show.html", context)
