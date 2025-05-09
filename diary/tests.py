from django.urls import reverse
from django.test import TestCase
from users.models import User
from .models import Note


class EntryViewsTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            email="test@mail.com",
            password="test12345",
        )
        self.client.login(email="test@mail.com", password="test12345")

    def test_entry_list_view(self):
        response = self.client.get(reverse("diary:entry_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "entry_list.html")

    def test_entry_create_view(self):
        response = self.client.post(
            reverse("diary:note_create"),
            {"title": "Test", "content": "test"},
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Note.objects.count(), 1)
        self.assertEqual(Note.objects.first().title, "Test")

    def test_entry_detail_view(self):
        note = Note.objects.create(
            title="Test", content="test", author=self.user
        )
        response = self.client.get(reverse("diary:note_detail", args=[note.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "note_detail.html")
        self.assertContains(response, "test")

    def test_entry_update_view(self):
        entry = Note.objects.create(
            title="Test", content="test", author=self.user
        )
        response = self.client.post(
            reverse("diary:note_edit", args=[entry.id]),
            {
                "title": "Updated",
                "content": "test NEW",
            },
        )
        self.assertEqual(response.status_code, 302)
        entry.refresh_from_db()
        self.assertEqual(entry.title, "Updated")

    def test_entry_delete_view(self):
        entry = Note.objects.create(
            title="Testdel", content="delete", author=self.user
        )
        response = self.client.post(reverse("diary:note_delete", args=[entry.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Note.objects.count(), 0)
