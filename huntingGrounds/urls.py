from django.urls import path
from . import views

urlpatterns =[
    path("hunting-grounds", views.grounds, name="hunting-grounds"),
    path("map", views.map, name="map")
]