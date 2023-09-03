from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import Contact


class ContactSerializer(ModelSerializer):
    # user = serializers.ReadOnlyField()

    class Meta:
        model = Contact
        fields = '__all__'