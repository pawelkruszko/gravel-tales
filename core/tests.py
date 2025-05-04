from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="John", email="john@email.com", password="testpassword12345"
        )
        self.assertEqual(user.username, "John")
        self.assertEqual(user.email, "john@email.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        AdminUser = User.objects.create_superuser(
            username="Admin", email="admin@email.com", password="testpassword12345"
        )
        self.assertEqual(AdminUser.username, "Admin")
        self.assertEqual(AdminUser.email, "admin@email.com")
        self.assertTrue(AdminUser.is_active)
        self.assertTrue(AdminUser.is_staff)
        self.assertTrue(AdminUser.is_superuser)
