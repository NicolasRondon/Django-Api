from django.db import models
import jwt
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


# Create your models here.

class UserManager(BaseUserManager):
    """
    Creando usuario
    """

    def create_user(self, username, email, password):
        if username is None:
            raise TypeError('Debe existir un username')

        if email is None:
            raise TypeError('Debe existir un email')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):
        """
        Creando Super Usuario
        """
        if password is None:
            raise TypeError('Debe existir una contraseña')

        user = self.create_superuser(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user
