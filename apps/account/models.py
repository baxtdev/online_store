from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField
from django_resized import ResizedImageField

from apps.account.managers import UserManager

# Create your models here.

class User(AbstractUser):
    phone=PhoneNumberField(
        'Телефон',
        unique=True,
    )
    image = ResizedImageField(
        upload_to='avatars/', 
        force_format='WEBP', 
        quality=90, 
        verbose_name="Фото",
        blank=True,
        null=True,
    ) 
    username = None
    middle_name = models.CharField(
        max_length=255, 
        verbose_name='Отчество',
        blank=True,
        null=True
        )
    last_activity = models.DateTimeField(
        verbose_name=_('last'),
        editable=True,
        blank=True,
        null=True
    )
    email = models.EmailField(
        _("Эл.почта"), 
        max_length=254,
        blank=True,
        null=True
        )
    GENDER_CHOICE = (
        ("M","Мужчина"),
        ("W","Женщина"),
    )
    gender = models.CharField(
        _("Пол"),
        choices = GENDER_CHOICE,
        max_length = 50,
        default = "NONE",
        blank=True,
        )
    date_of_birth = models.DateField(
        verbose_name=_('Дата рождения'),
        blank=True,
        null=True,
    )
    is_notifications = models.BooleanField(
        _('Отправлять уведомления'),
        default=False,
    )
    region = models.CharField(
        _("Регион"),
        max_length=255,
        blank=True,
        null=True,
    )
    
   
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'phone'
    

    objects = UserManager()
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['-id']
