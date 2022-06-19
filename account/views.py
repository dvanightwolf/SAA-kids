from django.shortcuts import render


def base(request):
    """Base page render."""
    return render(request, "base.html")