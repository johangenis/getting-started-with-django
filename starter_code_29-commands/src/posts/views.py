from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from .models import Entry, Blog
from .forms import BlogForm, BlogModelForm

def entry_list_view(request):
    entries = Entry.objects.all()
    blog_list = Blog.objects.all()
    context = {
        'post_list': entries,
        'blog_list': blog_list
    }
    return render(request, "post_list.html", context)


class EntryClassView(ListView):
    model = Entry
    context_object_name = 'post_list'
    template_name = 'post_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['newVariable'] = 1234
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

    
class EntryFormView(FormView):
    template_name = 'form.html'
    form_class = BlogModelForm
    success_url = '/'

    def form_valid(self, form):
        # form must send an email
        form.save()
        return super().form_valid(form)


def post_create(request):
    # form = BlogForm(request.POST or None)
    # if form.is_valid():
    #     name = form.cleaned_data.get('name')
    #     tagline = form.cleaned_data.get('tagline')
    #     blog = Blog(name=name, tagline=tagline)
    #     blog.save()
    #     return redirect('entries:entry-list')
    form = BlogModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('entries:entry-list')
    context = {
        'form': form
    }
    return render(request, 'form.html', context)