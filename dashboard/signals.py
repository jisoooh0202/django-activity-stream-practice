from django.contrib.auth.signals import (
    user_logged_in,
    user_logged_out,
    user_login_failed,
)
from actstream import action
from django.dispatch import receiver


@receiver(user_logged_in)
def track_login(sender, request, user, **kwargs):
    action.send(user, verb="logged in")
    print(
        "user {} logged in through page {}".format(
            user.username, request.META.get("HTTP_REFERER")
        )
    )


@receiver(user_logged_out)
def track_logout(sender, request, user, **kwargs):
    action.send(user, verb="logged out")
    print(
        "user {} logged out through page {}".format(
            user.username, request.META.get("HTTP_REFERER")
        )
    )


@receiver(user_login_failed)
def track_login_failed(sender, request, user, **kwargs):
    action.send(user, verb="login failed")
    print(
        "user {} failed to log in through page {}".format(
            user.username, request.META.get("HTTP_REFERER")
        )
    )


user_logged_in.connect(track_login)
user_logged_out.connect(track_logout)
user_login_failed.connect(track_login_failed)
