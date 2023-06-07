from django.contrib.auth.models import AnonymousUser
from .models import User
from djangochannelsrestframework.decorators import database_sync_to_async


def is_user_logged_in(user):
    return not isinstance(user, AnonymousUser)


@database_sync_to_async
def update_user_incr(user):
    if is_user_logged_in(user):
        User.objects.filter(pk=user.pk).update(online=True)


@database_sync_to_async
def update_user_decr(user):
    if is_user_logged_in(user):
        User.objects.filter(pk=user.pk).update(online=False)


class Online:

    async def connect(self):
        await self.accept()
        await update_user_incr(self.scope['user'])

    async def disconnect(self, code):
        await update_user_decr(self.scope['user'])