from user.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import Contact
from .serializers import ContactSerializer
from .views import ContactViewSet


class ContactViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(email='testuser@mail.ru', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.contact = Contact.objects.create(
            user=self.user,
            first_name='Иван',
            last_name='Иванов',
            phone='+79818324200',
            email='test_email@email.ru'
        )
        self.view = ContactViewSet.as_view({'get': 'retrieve'})

    def test_retrieve_contact(self):
        response = self.client.get(f'/phonebook/contact/{self.contact.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serialized_contact = ContactSerializer(self.contact)
        self.assertEqual(response.data, serialized_contact.data)

    def test_retrieve_nonexistent_contact(self):
        url = '/phonebook/contact/999/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, {'detail': 'Контакт не найден'})

    def test_create_contact(self):
        # Данные для создания нового контакта
        data = {
            'first_name': 'Алиса',
            'last_name': 'Уткина',
            'phone': '+798754321',
            'email': 'alice@gmail.com'
        }

        response = self.client.post('/phonebook/contact/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        contact = Contact.objects.get(pk=response.data['id'])
        self.assertEqual(contact.first_name, 'Алиса')
        self.assertEqual(contact.last_name, 'Уткина')
        self.assertEqual(contact.phone, '+798754321')
        self.assertEqual(contact.email, 'alice@gmail.com')

    def test_update_contact(self):
        contact = Contact.objects.create(
            user=self.user,
            first_name='Виктор',
            last_name='Бобров',
            phone='555555555',
            email='vikbobrov@yandex.ru'
        )

        data = {
            'first_name': 'Витя',
            'last_name': 'Бобриков',
        }

        response = self.client.put(f'/phonebook/contact/{contact.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        contact.refresh_from_db()
        self.assertEqual(contact.first_name, 'Витя')
        self.assertEqual(contact.last_name, 'Бобриков')

    def test_delete_contact(self):
        contact = Contact.objects.create(
            user=self.user,
            first_name='Артём',
            last_name='Башмаков',
            phone='+7123456789',
            email='artem@email.com'
        )

        response = self.client.delete(f'/phonebook/contact/{contact.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        with self.assertRaises(ObjectDoesNotExist):
            Contact.objects.get(pk=contact.id)

