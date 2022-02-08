import uuid
from pathlib import Path

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from phone_field import PhoneField

from taichi_dfw.resources.models import Resource
from taichi_dfw.styles.models import Style


def profile_pic_path(instance, filename):
    path = Path(filename)
    return f"profile_pics/{uuid.uuid4()}{path.suffix}"


class User(AbstractUser):
    """Default user for dfwtaichi."""

    #: First and last name do not cover name patterns around the globe
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    gmail = models.EmailField(
        "GMail address",
        blank=True,
        max_length=200,
        help_text="GMail address, used for authentication.",
    )
    phone = PhoneField("home phone.", blank=True)
    cell = PhoneField(
        "cell phone", blank=True, help_text="Number used for text notifications"
    )
    bio = models.TextField("TaiChi biography.", blank=True)
    biophoto = models.ImageField(upload_to=profile_pic_path, blank=True, default="")
    resources = models.ManyToManyField(to=Resource)
    favorite_style = models.ForeignKey(
        to=Style,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Select your default TaiChi Style.",
    )
    city = models.CharField(
        "City of residence.",
        max_length=30,
        help_text="Preferred city for TaiChi meetings.",
        blank=True,
        null=True,
    )
    leaderFlag = models.BooleanField("User is a leader", default=False)
    sponsor = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="User who applied leader designation.",
    )

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
