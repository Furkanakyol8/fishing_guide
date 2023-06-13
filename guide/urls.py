from django.urls import path
from . import views

urlpatterns =[
    path("guide", views.guide, name="guide"),
    path("guides/<slug:guide_slug>", views.guide_detail, name="guide_detail")
]