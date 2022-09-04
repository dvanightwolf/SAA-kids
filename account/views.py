from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, ArticleContent, Comment, Profile, Gallery, Slide
from .forms import CommentForm
from .ArticleClass import Articles
from taggit.models import Tag


def article_search(request):
    results = []
    article_list = Article.objects.all().order_by('-id')
    tags = Tag.objects.all()
    tag = Tag()
    query = None
    if request.method == 'GET':
        query = request.GET.get('search')
        tag_id = request.GET.get('tag', 'None')
        if tag:
            tag = Tag.objects.filter(pk=tag_id)
        if query != '':
            if Article.objects.filter(Q(tags__name=query)):
                results = Article.objects.filter(Q(tags__name=query))
            else:
                results = Article.objects.filter(Q(title__icontains=query))
        elif query == '' or tag == "0":
            results = Article.objects.all()

        if tag_id != '0':
            results = results.filter(Q(tags__name=tag[0].name))

    return render(request, 'ArticleArchives.html', {'articles': results, 'tags': tags, 'list': article_list})


def article(request):
    articles = Article.objects.all().order_by('-id')
    tags = Tag.objects.all()
    context = {"articles": articles, 'tags': tags}
    return render(request, 'ArticleArchives.html', context)


def base(request):
    """Base page render."""
    article_list = []
    articles = Article.objects.all()
    slide = None
    for s in Slide.objects.all():
        slide = s
        break
    slide_photo_1 = None
    slide_photo_2 = None
    slide_photo_3 = None
    slide_photo_4 = None
    if slide:
        slide_photo_1 = slide.photo_1.url
        slide_photo_2 = slide.photo_2.url
        slide_photo_3 = slide.photo_3.url
        slide_photo_4 = slide.photo_4.url
    photo = None
    for g in Gallery.objects.all():
        photo = g
        break
    index = 0
    for art in articles:
        index += 1
        article_list.append(Articles(index, art))

    context = {"articles": article_list, "photo": photo, 'slide_photo_1': slide_photo_1,
               'slide_photo_2': slide_photo_2, 'slide_photo_3': slide_photo_3,
               'slide_photo_4': slide_photo_4}
    return render(request, "home.html", context)


def article_details(request, article_id, slug):
    article = get_object_or_404(Article, pk=article_id, slug=slug)
    comments = Comment.objects.filter(article=article).order_by('-id')
    article_contents = ArticleContent.objects.filter(article=article)
    user = Profile()
    users = Profile.objects.all()
    for u in users:
        user = u
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.article = get_object_or_404(Article, pk=article_id)
            new_form.save()
            return redirect(article.get_url())
    else:
        form = CommentForm()
    context = {"article": article, "comments": comments,
               "user": user, "article_contents": article_contents, "form": form}
    return render(request, 'article_details.html', context)


def contact(request):
    return render(request, 'contact/contact.html')

def no_page_found(request, exception):
    error_id = '404'
    return render(request, 'error_page.html', {'error_id': error_id})


def bad_request(request, exception):
    error_id = '400'
    return render(request, 'error_page.html', {'error_id': error_id})


def forbidden(request, exception):
    error_id = '403'
    return render(request, 'error_page.html', {'error_id': error_id})


def server_error(request, exception):
    error_id = '500'
    return render(request, 'error_page.html', {'error_id': error_id})
