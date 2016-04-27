# coding: utf-8

from __future__ import unicode_literals
import datetime
from django.utils import timezone
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from textform.models import Message
from django.contrib.auth.models import User
from login.models import UserProfile
from django.dispatch import receiver
from .tasks import send_email_notification

@python_2_unicode_compatible
class Comment(models.Model):
    PUBLISH_OPTIONS = (
        ('y', 'yes'),
        ('n', 'no'),
    )

    message = models.ForeignKey(Message, null=True, blank=True, on_delete=models.CASCADE)
    text = models.TextField(verbose_name=u'Текст комментария')
    author = models.ForeignKey(User, null=True, blank=True, verbose_name=u'Автор комментария')
    pub_date = models.DateTimeField(verbose_name=u'Дата создания комментария', auto_now_add=True)
    is_published = models.CharField(max_length=1, choices=PUBLISH_OPTIONS)

    def __str__(self):
        return self.text

    def comment_beginning(self):
        return self.text[:20]


@receiver(models.signals.post_save, sender=Comment)
def on_comment_creation(sender, instance, *args, **kwargs):
    if kwargs.get('created'):
        comment = instance
        send_email_notification.delay(
            'gaintseva@phystech.edu',
            'New comment on question "{}"'.format(comment.message.title),
            'You got comment with the text: "{}"'.format(comment.text)
        )
