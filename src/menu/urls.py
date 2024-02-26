from django.urls import path

from .views import index, item

urlpatterns = [
    path('', index),
    path('<slug:item_slug>/', item, name="item"),
]