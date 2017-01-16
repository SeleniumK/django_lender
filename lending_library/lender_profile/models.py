from django.db import models
from django.contrib.auth.models import User
import uuid

from django.db.models.signals import post_save
from django.dispatch import receiver


class PatronProfile(models.Model):
    """Model representing User Profile (Patron Profile)."""

    user = models.OneToOneField(
        User,
        related_name="profile",
        on_delete=models.CASCADE
    )
    money_owed = models.DecimalField(max_digits=8, decimal_places=2, blank=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    library_id = models.UUIDField(default=uuid.uuid4, editable=False)


@receiver(post_save, sender=User)
def make_user_profile(sender, instance, **kwargs):
    """Create Patron Profile after new User is saved."""
    pass
