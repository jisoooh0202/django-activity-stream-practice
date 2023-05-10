from django.urls import path
from dashboards import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
]
