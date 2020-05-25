from django.urls import path, re_path
from .views import dummy_view

urlpatterns = [
    path("", dummy_view, name="entry-list"),
    path("<id>/", dummy_view, name="entry-detail"),
    re_path("(?P<id>[0-9]{4}/$)", dummy_view, name="entry-detail"),
    path("<int:id>/delete/", dummy_view, name="entry-delete"),
    path("<id>/update/", dummy_view, name="entry-update"),
]

# post - title: 'New world champion programmer'
#      - slug: 'wwww.yourdomain.com/articles/new-world-champion-programmer'
