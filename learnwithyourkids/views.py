from django.shortcuts import render
from .models import LearnWithYourKids
from django.db.models import Q
from taggit.models import Tag


def search(request):
    results = []
    lwyks_list = LearnWithYourKids.objects.all().order_by('-id')
    tags = Tag.objects.all()
    tag = Tag()
    query = None
    if request.method == 'GET':
        query = request.GET.get('search')
        tag_id = request.GET.get('tag', 'None')
        if tag:
            tag = Tag.objects.filter(pk=tag_id)
        if query != '':
            if LearnWithYourKids.objects.filter(Q(tags__name=query)):
                results = LearnWithYourKids.objects.filter(Q(tags__name=query))
            else:
                results = LearnWithYourKids.objects.filter(Q(title__icontains=query) |
                                                           Q(description__icontains=query))
        elif query == '' or tag == "0":
            results = LearnWithYourKids.objects.all()

        if tag_id != '0':
            results = results.filter(Q(tags__name=tag[0].name))

    return render(request, 'LWYK_show.html', {'lwyks': results, 'tags': tags, 'list': lwyks_list})


def show(request):
    lwyks = LearnWithYourKids.objects.all().order_by('-id')
    lwyks_list = LearnWithYourKids.objects.all().order_by('-id')
    tags = Tag.objects.all()
    context = {'lwyks': lwyks, 'tags': tags, 'list': lwyks_list}
    return render(request, 'LWYK_show.html', context)


