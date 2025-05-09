from django import forms

from diary.models import Note


class NoteForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = ["title", "content"]
