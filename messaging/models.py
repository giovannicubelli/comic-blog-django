from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    subject = models.CharField(max_length=150, blank=True) # Opcional, podría ser para iniciar una conversación
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"De: {self.sender.username} Para: {self.recipient.username} - {self.subject if self.subject else self.body[:30]}"

    class Meta:
        ordering = ['-timestamp']