from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone')
        error_messages = {
            'email': {
                'unique': 'Пользователь с таким email уже существует.',
                'required': 'Поле email обязательно для заполнения.',
            },
            'phone': {
                'required': 'Поле номера телефона обязательно для заполнения.',
            },
            'first_name': {'Вы не ввели имя контакта'}
        }