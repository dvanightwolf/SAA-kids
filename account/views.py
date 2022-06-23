from django.shortcuts import render, get_object_or_404
from .models import Article, Comment


def base(request):
    """Base page render."""
    articles = Article.objects.all()
    context = {"articles": articles}
    return render(request, "base.html", context)


def article_details(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    comments = Comment.objects.filter(article=article)
    context = {"article": article, "comments": comments}
    return render(request, 'article_details.html', context)

def no_page_found(request, exception):
    return render(request, 'no_page_found.html')
