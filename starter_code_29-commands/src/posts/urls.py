from django.urls import path, re_path

from .views import entry_list_view, EntryClassView, post_create, EntryFormView

app_name = 'posts'

urlpatterns = [
    path('', entry_list_view, name='entry-list'),
    path('create/', EntryFormView.as_view(), name='entry-create'),
    path('class-view/', EntryClassView.as_view(), name='entry-class-list')
]
