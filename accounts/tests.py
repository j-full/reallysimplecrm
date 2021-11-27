from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model

from .views import register

User = get_user_model()

class RegisterTests(TestCase):
    def setUp(self):
        self.response = self.client.get(reverse('register'))
        self.dashboard_response = self.client.get(reverse('dashboard'))

    def test_register_resolve_view(self):
        self.assertEquals(resolve('/accounts/register/').func, register)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')


class SuccessfulRegisterTests(TestCase):
    def setUp(self):
        self.next_url = reverse('dashboard')
        data = {
            'username': 'joe',
            'email': 'joe@joe.com',
            'password1': 'abcdef123456',
            'password2': 'abcdef123456'
        }
        self.response = self.client.post(reverse('register'), data)

    def test_redirection(self):
        self.assertRedirects(self.response, self.next_url)

    def test_user_creation(self):
        self.assertTrue(User.objects.exists())

    def test_user_authentication(self):
        response = self.client.get(self.next_url)
        user = response.context.get('user')
        self.assertTrue(user.is_authenticated)

class ErrorRegisterTests(TestCase):
    def setUp(self):
        self.response = self.client.post(reverse('register'), {})

    def test_form_errors(self):
        form = self.response.context.get('form')
        self.assertTrue(form.errors)

    def test_dont_create_user(self):
        self.assertFalse(User.objects.exists())

class AuthTests(TestCase):
    def setUp(self):
        User.objects.create_user(username='joe', email='joe@joe.com', password='12345678')
        self.client.login(username='joe', password='12345678')
        self.response = self.client.get(reverse('dashboard'))

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

class NotAuthTests(TestCase):
    def setUp(self):
        self.url = reverse('dashboard')
        self.response = self.client.get(self.url)
    
    def test_status_code(self):
        self.assertEquals(self.response.status_code, 302)
    
    def test_redirection(self):
        login_url = reverse('login')
        self.assertRedirects(self.response, f'{login_url}?next={self.url}')