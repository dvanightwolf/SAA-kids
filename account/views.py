from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, ArticleContent, Comment, Profile, Gallery, Slide
from .forms import CommentForm


def base(request):
    """Base page render."""
    articles = Article.objects.all()
    slide = Slide.objects.all()
    photos = Gallery.objects.all()
    article_contents = ArticleContent.objects.all()
    context = {"articles": articles, "photos": photos, 'slide':slide}
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
            return redirect("home")
    else:
        form = CommentForm()
    context = {"article": article, "comments": comments, "user": user, "article_contents": article_contents, "form": form}
    return render(request, 'article_details.html', context)


def no_page_found(request, exception):
    return render(request, 'no_page_found.html')
