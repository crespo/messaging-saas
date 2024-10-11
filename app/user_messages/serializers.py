from rest_framework import serializers
from core.serializers import CompanySafeSerializerMixin
from .models import UserMessage


class UserMessageSerializer(
    CompanySafeSerializerMixin, serializers.HyperlinkedModelSerializer
):
    class Meta:
        model = UserMessage
        fields = (
            "id",
            "url",
            "from_user",
            "to_user",
            "text",
            "date",
        )

        read_only_fields = ("from_user",)
