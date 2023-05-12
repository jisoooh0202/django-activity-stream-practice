from django.views import generic
from .models import MyAction


class MyActionStreamView(generic.ListView):
    model = MyAction
    template_name = "dashboards/dashboard.html"
    context_object_name = "action_list"

    def get_queryset(self):
        # Use custom manager methods or filters for CustomActionManagerOne
        return MyAction.objects.all()
