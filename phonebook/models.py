from rest_framework.exceptions import ValidationError

from user.models import User
from django.db import models


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contact', verbose_name='Пользователь',
                             blank=True, null=True)
    first_name = models.CharField(max_length=20, blank=True, null=True, verbose_name='Имя')
    last_name = models.CharField(max_length=30, blank=True, null=True, verbose_name='Фамилия')
    phone = models.CharField( max_length=15, blank=True, null=True, verbose_name='Номер телефона')
    email = models.EmailField(max_length=40, blank=True, null=True, verbose_name='Email')

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return f'{self.first_name}, {self.last_name}, {self.phone}, {self.email}'


