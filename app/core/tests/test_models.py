from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email(self):
        """Test creating a user mail"""
        email = "kripa@gmail.com"
        pwd = "12345"
        user = get_user_model().objects.create_user(
            email=email, 
            password=pwd
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.password, pwd)
    
    def test_new_user_email_normalized(self):
        """test new mail for normalize"""

        email = "kapil@gmail.com"
        user = get_user_model().objects.create_user(email, "1234")

        self.assertEqual(user.email, email) 

   #def test_email_user_invalid_email(self):
    #     """ invalid user email """
    #    with self.assertRaises(ValueError):
    #        get_user_model().objects.create_user("ok", "12345")
    

    def test_create_new_super_user(self):
        """ create super user """
        user = get_user_model().objects.create_superuser("k@gmail.com","12345")

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
