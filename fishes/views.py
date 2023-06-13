from django.shortcuts import render, get_object_or_404
from .forms import SearchForm
from fishes.models import Fishes, Category

def fishes(request):
    context = {
        "fishes": Fishes.objects.all(),
        "categories": Category.objects.all()
    }
    return render(request, "fishes/fishes.html", context)

def fish_details(request):
    return render(request, "fishes/fish-details.html")

def fish_tactics(request, slug):
    fish = get_object_or_404(Fishes, slug=slug)
    return render(request, 'fishes/fish_tactics.html', {'fish': fish})

def season(request):
    return render(request, "fishes/season.html")

def sizes(request):
    return render(request, "fishes/sizes.html")

def fishes_by_category(request, slug):
    context = {
        "fishes": Fishes.objects.filter(category__slug=slug),
        "categories": Category.objects.all()
    }
    return render(request, "fishes/fishes.html", context)

def search(request):
    form = SearchForm(request.GET)
    results = []

    if form.is_valid():
        search_query = form.cleaned_data['search_query']
        results = Fishes.objects.filter(name__icontains=search_query)

    return render(request, 'fishes/search.html', {'form': form, 'results': results})




