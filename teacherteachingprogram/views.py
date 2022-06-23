from django.shortcuts import render, get_object_or_404
from .models import TTP, Day, Photo, Material
import calendar
from calendar import HTMLCalendar


def display(request):
    """List all workshops."""
    # Get all ttp.
    ttp = TTP.objects.all()
    days = Day.objects.all()
    photos = Photo.objects.all()
    material = Material.objects.all()
    # Put the info in a dictionary.
    context = {"ttp": ttp, "days": days, "photos": photos, "material": material}
    # Render show page and send the dictionary to it.
    return render(request, "ttp_display.html", context)


def ttp_details(request, ttp_id, ttp_slug):
    ttp = get_object_or_404(TTP, pk=ttp_id, slug=ttp_slug)
    days = Day.objects.filter(ttp_id=ttp)
    photos = Photo.objects.filter(ttp_id=ttp)
    materials = Material.objects.filter(ttp_id=ttp)
    context = {"ttp": ttp, 'days': days, "photos": photos, 'materials': materials}
    return render(request, "ttp_details.html", context)


