from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from users.managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

NULLABLE = {'blank': True, 'null': True}


class UserRoles:
    ADMIN = 'admin'
    USER = 'user'


class User(AbstractBaseUser):

    ROLE_CHOICES = [
        (UserRoles.ADMIN, 'admin'),
        (UserRoles.USER, 'user'),
    ]
    email = models.EmailField(unique=True, verbose_name='Email')
    password = models.CharField(max_length=128, verbose_name='Password')
    last_login = models.DateTimeField(auto_now_add=True, verbose_name='last_login', **NULLABLE)
    phone = models.CharField(max_length=20, verbose_name='Phone')
    role = models.CharField(max_length=20, default=UserRoles.USER, choices=ROLE_CHOICES, verbose_name='Role')
    first_name = models.CharField(max_length=20, verbose_name='first_name')
    last_name = models.CharField(max_length=20, verbose_name='last_name')
    is_active = models.BooleanField(default=True, verbose_name='is_active')
    image = models.ImageField(upload_to='users/', **NULLABLE, verbose_name='image')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    objects = UserManager()

