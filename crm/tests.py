from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from . models import Contact, PostCard

User = get_user_model()

class ContactTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='joe', email='joe@joe.com', password='12345678')
        self.contact = Contact.objects.create(created_by=self.user, first_name='Homer', last_name='simpson')
        self.url_new = reverse('contact_new')
        self.contact_url = reverse('contact_detail', kwargs={'pk': self.contact.pk})
        self.client.login(username='joe', password='12345678')


class NewContactTest(ContactTestCase):
    
    def test_auth_status(self):
        self.client.logout()
        self.assertEquals(self.client.get(self.url_new).status_code, 302)

    def test_contact_creation(self):
        self.assertTrue(Contact.objects.exists())
    
    def test_detail_view(self):
        response = self.client.get(reverse('contact_detail', kwargs={'pk':self.contact.id}))
        self.assertEqual(response.status_code, 200)

    def test_required_first_and_last_name(self):
        self.contact.first_name = ''
        self.assertRaises(ValidationError, self.contact.full_clean)

class NotOwnerContactTest(ContactTestCase):
    def setUp(self):
        super().setUp()
        username, password = 'tim', '12345678'
        User.objects.create_user(username=username, password=password)
        self.client.login(username=username, password=password)
        self.response = self.client.get(self.contact_url)
    
    def test_status_code(self):
        self.assertEquals(self.response.status_code, 403)

class MakePostCardTest(ContactTestCase):
    def setUp(self):
        super().setUp()
        from django.utils import timezone
        PostCard.objects.create(contact=self.contact, time_sent=timezone.now())
    
    def test_make_postcard(self):
        self.assertTrue(PostCard.objects.exists())

