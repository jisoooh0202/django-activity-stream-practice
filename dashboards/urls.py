from django.urls import path
from dashboards import views

urlpatterns = [
    path("", views.MyActionStreamView.as_view(), name="dashboard"),
]
