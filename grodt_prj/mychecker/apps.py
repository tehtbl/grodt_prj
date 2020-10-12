from django.apps import AppConfig


class MyCheckerConfig(AppConfig):

    name = "mychecker"
    verbose_name = "MyChecker Module"

    def ready(self):
        pass
        # load_mychecker_settings()
        # from . import handlers  # NOQA:F401
