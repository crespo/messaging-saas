from django.contrib.auth import get_user_model
from django.db import models

from core.models import CompanyRelatedModel


User = get_user_model()


class UserMessage(CompanyRelatedModel):
    text = models.TextField('message', blank=False, null=False)
    date = models.DateTimeField('date', auto_now_add=True)
    from_user = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)

    class Meta:
        db_table = 'user_messages'
        ordering = ['date']