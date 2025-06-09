from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save # Para crear perfil automáticamente
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # nombre = models.CharField(max_length=100, blank=True) # User ya tiene first_name
    # apellido = models.CharField(max_length=100, blank=True) # User ya tiene last_name
    # email ya está en User
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, default='avatars/default_avatar.png')
    biografia = models.TextField(blank=True, null=True)
    link_web = models.URLField(max_length=200, blank=True, null=True)
    # fecha_cumpleanios = models.DateField(null=True, blank=True) # Opcional

    def __str__(self):
        return f'Perfil de {self.user.username}'

# Señal para crear/actualizar el perfil automáticamente cuando se crea/actualiza un User
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save() # Guardar perfil existente si se actualiza el User