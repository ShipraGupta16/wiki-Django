from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.wikientry, name="wikientry"),
    path("search/", views.search, name="search_results"),
    path("create/", views.create, name="create"),
    path("<str:name>/edit/", views.edit, name="edit"),
    path("random/", views.randomEntries, name="random")
]

