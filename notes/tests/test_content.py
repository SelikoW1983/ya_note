from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from notes.models import Note

User = get_user_model()


class TestCreatePage(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.create_url = reverse('notes:add')
        cls.author = User.objects.create(username='Комментатор')
        cls.notes = Note.objects.create(
            title='Тестовая новость',
            text='Просто текст.',
            author=cls.author,
        )

    def test_anonymous_client_has_no_form(self):
        response = self.client.get(self.create_url)
        self.assertNotIn('form', response.context)

    def test_authorized_client_has_form(self):
        self.client.force_login(self.author)
        response = self.client.get(self.create_url)
        self.assertIn('form', response.context)
