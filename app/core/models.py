from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin



class UserManager(BaseUserManager):
    
    def create_user(self, email, password=None, **kwargs):
        """Create and saves New User"""

        if not email:
            raise ValueError("User must have email address")
        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email,password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    """ custom user model """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    



