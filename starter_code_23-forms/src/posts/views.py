from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Entry


def entry_list_view(request):
    entries = Entry.objects.all()
    context = {"post_list": entries}
    return render(request, "post_list.html", context)


class EntryClassView(ListView):
    model = Entry
    context_object_name = "post_list"
    template_name = "post_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["newVariable"] = 1234
        return context

    def get_queryset(self):
        # filtering
        return Entry.objects.all()[0:1]


class EntryClassDetailView(DetailView):
    model = Entry

    def get_object(self):
        obj = super().get_object()
        # perform logic
        return obj
