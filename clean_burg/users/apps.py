from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "clean_burg.users"
    verbose_name = _("Пользователи")

    def ready(self):
        try:
            import clean_burg.users.signals  # noqa F401
        except ImportError:
            pass
