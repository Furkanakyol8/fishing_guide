from django.shortcuts import render
from fishes.models import Fishes
from fishes.models import Category


def home(request):
    context = {
        "categories": Category.objects.all()
    }
    return render(request, "homepage/index.html", context)
