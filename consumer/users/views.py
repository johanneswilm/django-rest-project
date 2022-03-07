import httpx
from asgiref.sync import sync_to_async

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.conf import settings


def get_local_users():
    return list(User.objects.all())


async def index(request):
    context = {}
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                "http://localhost:8000/users/users/",
                headers={"Authorization": f"Token {settings.AUTH_TOKEN}"},
            )
        json = response.json()
        context["remote_users"] = json["results"]
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
