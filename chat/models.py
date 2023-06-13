from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class Swipe(models.Model):
    '''
    Model for swipes data of user
    '''
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('Sender'),
        related_name='swipe_sender',
        on_delete=models.CASCADE,
    )
    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('Receiver'),
        related_name='swipe_receiver',
        on_delete=models.CASCADE,
    )
    like = models.BooleanField(
        verbose_name=_('Is swiped right'),
    )

    class Meta:
        unique_together = ('sender', 'receiver')


class Message(models.Model):
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('Sender'),
        related_name='message_sender',
        on_delete=models.CASCADE,
    )
    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('Receiver'),
        related_name='message_receiver',
        on_delete=models.CASCADE,
    )
    content = models.TextField(
        verbose_name=_('Message content'),
        max_length=300,
        default='',
        blank=False,
    )
    timestamp = models.DateTimeField(
        verbose_name=_('Sending time'),
        auto_now_add=True,
    )
    is_read = models.BooleanField(
        verbose_name=_('Is read'),
    )

    def __str__(self):
        return self.content

    class Meta:
        ordering = ('timestamp', )
