from django.shortcuts import render, redirect
from .forms import LearnWithYourKidsForm
# Create your views here.


def talon(request):
    print(121)
    if request.method == "POST":
        form = LearnWithYourKidsForm(request.POST, files=request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            if request.FILES:
                new_form.photo = request.FILES
                new_form.save()
                return redirect("../")
    else:
        form = LearnWithYourKidsForm()
    context = {"form": form}
    return render(request, "talon.html", context)

