from django.apps import AppConfig


class DashboardConfig(AppConfig):
    name = "dashboard"

    def ready(self):
        from actstream import registry
        from django.contrib.auth.models import User

        registry.register(User, self.get_model("Task"), self.get_model("Supervisor"))
