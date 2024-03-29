from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSIteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="admin@gmail.com", password="12345"
        )

        self.client.force_login(self.admin_user)

        self.user = get_user_model().objects.create_user(
            email="user@gmail.com", password="12345",
            name= "Test User"
        )
    
    def test_user_lists(self):
        """ Test that users are listed"""

        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)
        print(res)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)


