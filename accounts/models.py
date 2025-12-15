from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(to=User, related_name='profile', on_delete=models.CASCADE)
    phone=models.CharField(max_length=20, null=True, blank=True)
    email_verified=models.BooleanField(default=False)
    phone_verified=models.BooleanField(default=False)
    created_at=models.DateTimeField(default=timezone.now)
    updated_at=models.DateTimeField(auto_now=True)
    
    @receiver(post_save, sender=User)
    def on_save(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
    
    def __str__(self):
        return self.user.username