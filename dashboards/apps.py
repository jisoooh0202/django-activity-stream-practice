from django.apps import AppConfig


class DashboardsConfig(AppConfig):
    name = "dashboards"

    def ready(self):
        from actstream import registry
        from django.contrib.auth.models import User
        import dashboards.signals

        registry.register(User, self.get_model("Task"), self.get_model("Supervisor"))
