from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Chat(models.Model):
    users = models.ManyToManyField(User, related_name='chat')
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-modified_at']

class ChatMessage(models.Model):
    chat = models.ForeignKey(Chat, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_at']

    def save(self, *args, **kwargs):
        self.chat.save()
        super(ChatMessage,self).save(*args, **kwargs)
