from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "taichi_dfw.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import taichi_dfw.users.signals  # noqa F401
        except ImportError:
            pass
