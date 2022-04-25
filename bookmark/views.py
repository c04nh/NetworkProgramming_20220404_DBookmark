from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from bookmark.models import Bookmark


class BookmarkListView(ListView):
    model = Bookmark
    # bookmark_list.html, {'bookmark_list': Bookmark.objects.all()}

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['name', 'url']
    template_name_suffix = '_create'
    success_url = reverse_lazy('bookmark:list')

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['name', 'url']
    template_name_suffix = '_update'
    # success_url = reverse_lazy('bookmark:list')

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:list')