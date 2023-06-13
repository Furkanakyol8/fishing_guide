from django.shortcuts import render, get_object_or_404
from guide.models import Guide

def guide(request):
    context = {
        "guides": Guide.objects.all()
    }
    return render(request, "guide/guide.html", context)

def guide_detail(request, guide_slug):
    guide = get_object_or_404(Guide, slug=guide_slug)
    return render(request, "guide/guide_detail.html", {'guide': guide})