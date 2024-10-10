from rest_framework import permissions
from rest_framework import generics

from . import serializers
from .models import UserMessage


class UserMessageList(generics.ListCreateAPIView):
    name = 'usermessage-list'
    permission_classes = (
        permissions.IsAuthenticated,
    )
    serializer_class = serializers.UserMessageSerializer
    queryset = UserMessage.objects.all()

    def perform_create(self, serializer):
        company_id = self.request.user.company_id
        serializer.save(company_id=company_id)

    def get_queryset(self):
        company_id = self.request.user.company_id
        return super().get_queryset().filter(company_id=company_id)


class UserMessageDetail(generics.RetrieveAPIView):
    name = 'usermessage-detail'
    permission_classes = (
       permissions.IsAuthenticated,
    )
    serializer_class = serializers.UserMessageSerializer
    queryset = UserMessage.objects.all()

    def get_queryset(self):
        company_id = self.request.user.company_id
        return super().get_queryset().filter(company_id=company_id)