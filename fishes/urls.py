from django.urls import path
from . import views

urlpatterns =[
    path("fishes", views.fishes, name="fishes"),
    path("fish-details", views.fish_details),
    path("fishes/<slug:slug>", views.fishes_by_category, name="fishes_by_category"),
    path('search/', views.search, name='search'),
    path("sizes", views.sizes, name="sizes"),
    path("season", views.season, name="season"),
    path('fishes/<slug:slug>/tactics/', views.fish_tactics, name='fish_tactics')
]
