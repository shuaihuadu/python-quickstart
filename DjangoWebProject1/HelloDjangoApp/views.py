from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def index(request):
    now = datetime.now()

    return render(
        request,
        "HelloDjangoApp/index.html",
        {
            "title":"Hello Django",
            "message":"Hello Django!",
            "content": " on " + now.strftime("%A, %d %B, %Y at %X")
        },
    )