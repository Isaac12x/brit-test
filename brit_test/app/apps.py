from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class AppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "brit_test.app"
    verbose_name = _("App")

    def ready(self):
        try:
            import brit_test.app.signals  # noqa F401
        except ImportError:
            raise ImportError("Error importing app signals")
