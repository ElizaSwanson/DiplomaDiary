from django.urls import path

from .apps import DiaryConfig
from .views import (DiaryEntrySearchView, NotesCreateView, NotesDetailView, NotesListView, NotestDeleteView,
                    NotesUpdateView)

app_name = DiaryConfig.name

urlpatterns = [
    path("", NotesListView.as_view(), name="entry_list"),
    path("note/<int:pk>/edit/", NotesUpdateView.as_view(), name="note_edit"),
    path("note/<int:pk>/delete/", NotestDeleteView.as_view(), name="note_delete"),
    path("note/<int:pk>/", NotesDetailView.as_view(), name="note_detail"),
    path("note/create/", NotesCreateView.as_view(), name="note_create"),
    path("search/", DiaryEntrySearchView.as_view(), name="search"),
]
