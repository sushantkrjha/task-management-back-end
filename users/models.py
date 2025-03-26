from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    class Meta:
        verbose_name = "Custom User"
        verbose_name_plural = "Custom Users"

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="customuser_set",  # Changed related_name
        blank=True,
        help_text="The groups this user belongs to.",
    )

    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="customuser_permissions_set",  # Changed related_name
        blank=True,
        help_text="Specific permissions for this user.",
    )
