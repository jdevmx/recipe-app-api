from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_succeful(self):
        """Test creating a new user with an email is succeful"""
        email = 'test@test.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        """Test the email for a new user is normalized"""
        emai = 'test@DOMAIN.COM'
        user = get_user_model().objects.create_user(
            email=emai, password='1234')

        self.assertEqual(user.email, emai.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123456')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            email='test@TEST.com',
            password='1236546'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
