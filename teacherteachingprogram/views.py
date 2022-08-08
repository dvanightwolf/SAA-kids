from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import TTP, Day, Photo, Material
from taggit.models import Tag


def search(request):
    results = []
    photos = Photo.objects.all()
    tags = Tag.objects.all()
    sal_tag = Tag()
    query = None
    if request.method == "GET":
        query = request.GET.get("search")
        tag = request.GET.get("tag_id")

        if tag:
            sal_tag = Tag.objects.filter(pk=tag)

        if query != '':

            if TTP.objects.filter(Q(tags__name__icontains=query)):
                results = TTP.objects.filter(Q(tags__name=query))
            else:
                results = TTP.objects.filter(Q(title__icontains=query) |
                                             Q(description__icontains=query))

        elif query == '':
            results = TTP.objects.all().order_by('-id')

        if tag != "0":
            results = results.filter(Q(tags__name=sal_tag[0].name))

    return render(request, 'ttp_display.html', {'ttp': results, 'tags': tags, "photos": photos})


def display(request):
    """List all workshops."""
    # Get all ttp.
    tags = Tag.objects.all()
    ttp = TTP.objects.all().order_by('-id')
    days = Day.objects.all()
    photos = Photo.objects.all()
    material = Material.objects.all()
    # Put the info in a dictionary.
    context = {"ttp": ttp, 'tags': tags, "days": days, "photos": photos, "material": material}
    # Render show page and send the dictionary to it.
    return render(request, "ttp_display.html", context)


def ttp_details(request, ttp_id, ttp_slug):
    ttp = get_object_or_404(TTP, pk=ttp_id, slug=ttp_slug)
    days = Day.objects.filter(ttp_id=ttp)
    photos = Photo.objects.filter(ttp_id=ttp)
    materials = Material()
    materials_show = False
    visible = True
    if not ttp.lock:
        materials = Material.objects.filter(ttp_id=ttp)
        materials_show = True
        visible = False
    if request.method == "POST":
        code = request.POST.get('code')
        if code == ttp.material_password:
            visible = False
            materials_show = True
            materials = Material.objects.filter(ttp_id=ttp)

    context = {"ttp": ttp, 'days': days, "photos": photos, 'materials_show': materials_show,
               'materials': materials, 'visible': visible}
    return render(request, "ttp_details.html", context)
