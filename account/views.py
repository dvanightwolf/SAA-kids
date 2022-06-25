from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Comment, Profile
from .forms import CommentForm


def base(request):
    """Base page render."""
    articles = Article.objects.all()
    context = {"articles": articles}
    return render(request, "home.html", context)


def article_details(request, article_id, slug):
    article = get_object_or_404(Article, pk=article_id, slug=slug)
    comments = Comment.objects.filter(article=article)
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
    context = {"article": article, "comments": comments, "user": user, "form": form}
    return render(request, 'article_details.html', context)


def no_page_found(request, exception):
    return render(request, 'no_page_found.html')
