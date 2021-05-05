import datetime

from django.test import TestCase
from django.urls import reverse, resolve

from .models import Message


class HomeTests(TestCase):

    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_messages(self):
        resp = self.client.get('/messages')
        self.assertEqual(resp.status_code, 200)

    def test_messages(self):
        resp = self.client.get('/admin')
        self.assertEqual(resp.status_code, 301)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.view_name, 'home')

    def test_home_url_resolves_message_view(self):
        view = resolve('/messages')
        self.assertEquals(view.view_name, 'messages')


class MessagesModelTests(TestCase):

    def setUp(self):
        self.mes = Message.objects.create(
                title="test title",
                body="test body",
                date=datetime.date.today()
            )

    def test_model_title(self):
        self.assertEqual(str(self.mes), 'test title')
