from django.contrib.auth.signals import (
    user_logged_in,
    user_logged_out,
    user_login_failed,
)
from actstream import action


def track_login(sender, request, user, **kwargs):
    action.send(user, verb="logged in")


def track_logout(sender, request, user, **kwargs):
    action.send(user, verb="logged out")


def track_login_failed(sender, request, user, **kwargs):
    action.send(user, verb="login failed")


user_logged_in.connect(track_login)
user_logged_out.connect(track_logout)
user_login_failed.connect(track_login_failed)
