from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, filters

from .models import Contact
from .serializers import ContactSerializer


class ContactViewSet(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'first_name', 'last_name', 'email', 'phone']
    ordering_fields = ['id', 'first_name', 'last_name', 'email', 'phone']
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Contact.objects.filter(user=self.request.user).order_by('id')

    def retrieve(self, request, *args, **kwargs):
        try:
            contact = self.get_queryset().get(pk=kwargs['pk'])
        except (NotFound, ObjectDoesNotExist):
            raise NotFound("Контакт не найден")

        serializer = self.get_serializer(contact)
        return Response(serializer.data)
