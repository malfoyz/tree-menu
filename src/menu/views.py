from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    """Обработчик главной страницы."""

    return render(
        request=request,
        template_name='menu/index.html',
    )


def item(request: HttpRequest, item_slug: str) -> HttpResponse:
    """Обработчик страницы пункта меню."""

    return render(
        request=request,
        template_name='menu/index.html',
    )

