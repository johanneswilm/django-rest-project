import httpx

from django.shortcuts import render
from django.http import HttpResponse

async def index(request):
    async with httpx.AsyncClient() as client:
        response = await client.get("http://localhost:8000/users/users/", auth=('admin', 'password'))
    users = response.json()
    return render(request, 'users/index.html', {'users': users})
