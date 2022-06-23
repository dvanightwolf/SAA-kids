from django.shortcuts import render, get_object_or_404
from .models import Activity, ActivityPhoto
import calendar
from taggit.models import Tag
from django.db.models import Q


def search(request):
    results = []
    tags = Tag.objects.all()
    tag = Tag()
    query = None
    if request.method == 'GET':
        query = request.GET.get('search')
        tag_id = request.GET.get('tag', 'None')
        if tag:
            tag = Tag.objects.filter(pk=tag_id)
        if query != '':
            if Activity.objects.filter(Q(tags__name=query)):
                results = Activity.objects.filter(Q(tags__name=query))
            else:
                results = Activity.objects.filter(Q(title__icontains=query) |
                                                  Q(description__icontains=query))
        elif query == '' or tag == "0":
            results = Activity.objects.all()

        if tag_id != '0':
            results = results.filter(Q(tags__name=tag[0].name))

    return render(request, 'activities.html', {'activity': results, 'tags': tags})


def display(request):
    activity = Activity.objects.all().order_by('-id')
    tags = Tag.objects.all()
    context = {'activity': activity, 'tags': tags}
    return render(request, 'activities.html', context)


def act_details(request, activity_id, activity_slug):
    activity = get_object_or_404(Activity, pk=activity_id, slug=activity_slug)
    photos = ActivityPhoto.objects.filter(activity_id=activity)
    context = {"activity": activity, "photos": photos}
    return render(request, "activity_details.html", context)


def calender(request, year, month):
    act = Activity.objects.get(pk=1)
    month = month.title()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    print(list(calendar.month_name))
    print(act.date.weekday())

    return render(request, 'calendar.html', {'year': year, 'month': month, 'month_number': month_number,
                                             })
