from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import NoteForm
from .models import Note


class DiaryEntrySearchView(LoginRequiredMixin, ListView):
    model = Note
    template_name = "search.html"  # Убедитесь в правильном пути
    context_object_name = "notes"

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Note.objects.filter(
                Q(title__icontains=query) | Q(content__icontains=query),
                author=self.request.user,
            ).order_by("-created_at")
        return Note.objects.filter(author=self.request.user).order_by("-created_at")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get("q", "")
        return context


class NotesListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = "entry_list.html"
    context_object_name = "notes"

    def get_queryset(self):
        return Note.objects.filter(author=self.request.user).order_by("-created_at")


class NotesDetailView(LoginRequiredMixin, DetailView):
    model = Note
    template_name = "note_detail.html"

    def get_queryset(self):
        return Note.objects.filter(author=self.request.user)


class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Note
    form_class = NoteForm
    template_name = "note_form.html"
    success_url = reverse_lazy("diary:entry_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class NotesUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    form_class = NoteForm
    template_name = "note_form.html"
    success_url = reverse_lazy("diary:entry_list")

    def get_queryset(self):
        return Note.objects.filter(author=self.request.user)


class NotestDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = "note_delete.html"
    success_url = reverse_lazy("diary:entry_list")

    def get_queryset(self):
        return Note.objects.filter(author=self.request.user)
