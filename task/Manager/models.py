from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


#Token Imports
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Tasks(models.Model):
    CHOICES = (('pending', 'Pending'),
                ('running','Running'),
                ('completed','Completed')
              )

    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    due_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=CHOICES, default='running', max_length=100)
    owner = models.ForeignKey('auth.User',  related_name='tasks', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['created']