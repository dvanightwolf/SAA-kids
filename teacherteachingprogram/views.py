from django.shortcuts import render, get_object_or_404
from .models import TTP, Day, Photo, Material
from .forms import CheckForm
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
    materials = list()

    if request.method == "POST":
        code = request.POST.get('code')
        if code == ttp.material_password:
            days = Day.objects.filter(ttp_id=ttp)
            photos = Photo.objects.filter(ttp_id=ttp)
            materials = Material.objects.filter(ttp_id=ttp)
            context = {"ttp": ttp, 'days': days, "photos": photos, 'materials': materials}
            return render(request, 'ttp_details.html', context)

    context = {"ttp": ttp, 'days': days, "photos": photos, 'materials': materials}
    return render(request, "ttp_details.html", context)


''' materials = Material()
    code = str()
    days = Day()
    photos = Photo()
    if request.method == "GET":
        code = request.GET.get('code')
        print(code)
        if code == ttp.material_password:
            print(code)
            days = Day.objects.filter(ttp_id=ttp)
            photos = Photo.objects.filter(ttp_id=ttp)
            materials = Material.objects.filter(ttp_id=ttp)
            context = {"ttp": ttp, 'days': days, "photos": photos, 'materials': materials}
            return render(request, 'ttp_details.html', context)
    else:'''


def check(request, ttp_id):

    materials = Material()
    if request.method == 'GET':

        code_field = request.GET.get('code')

        ttp = get_object_or_404(TTP, pk=ttp_id)
        if ttp.material_password == code_field:

            materials = Material.objects.filter(ttp_id=ttp)
    return render(request, "ttp_details.html", {'materials': materials})





