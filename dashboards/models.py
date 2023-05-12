from .managers import MyActionManager
from actstream.models import Action


class MyAction(Action):
    objects = MyActionManager()

    class Meta:
        proxy = True
