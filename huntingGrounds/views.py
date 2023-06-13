from django.shortcuts import render
from huntingGrounds.models import Grounds

def grounds(request):
    context = {
        "grounds": Grounds.objects.all()
    }
    return render(request, "huntingGrounds/hunting-grounds.html", context)

def map(request):
    return render(request, "huntingGrounds/map.html")
