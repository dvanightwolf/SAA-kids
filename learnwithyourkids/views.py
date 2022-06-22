from django.shortcuts import render, get_object_or_404
from .models import LearnWithYourKids


def show(request):
    """Show all learn."""
    # Get all learn.
    learn = LearnWithYourKids.objects.all()
    # Put the info in a dictionary.
    context = {"learn": learn}
    # Render show page and send the dictionary to it.
    return render(request, "show.html", context)


def details(request, learn_id):
    """Show workshop details."""
    # Get learn by id.
    learn = get_object_or_404(LearnWithYourKids, pk=learn_id)
    # Put the info in a dictionary.
    context = {"learn": learn}
    # Render details page and send the dictionary to it.
    return render(request, "details.html", context)
