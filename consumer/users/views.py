import httpx
from asgiref.sync import sync_to_async

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.conf import settings
from django.core.cache import cache


def get_local_users():
    users = cache.get("users")
    if not users:
        users = list(User.objects.all())
        cache.set("users", users, 15)
    return users


async def index(request):
    context = {}
    remote_users = await cache.aget("remote_users")
    if remote_users:
        context["remote_users"] = remote_users
    else:
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    "http://localhost:8000/users/users/",
                    headers={"Authorization": f"Token {settings.AUTH_TOKEN}"},
                )
            json = response.json()
            remote_users = json["results"]
            context["remote_users"] = remote_users
            await cache.aset("remote_users", remote_users, 15)
        except httpx.RequestError as exc:
            context["connection_error"] = True
    context["local_users"] = await sync_to_async(
        get_local_users, thread_sensitive=True
    )()
    return render(
        request,
        "users/index.html",
        context,
    )
