from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from accounts.models import Profile
from bookmark.models import Bookmark


class BookmarkListView(ListView):
    model = Bookmark
    # bookmark_list.html, {'bookmark_list': Bookmark.objects.all()}

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated: # 로그인하면 로그인한 사용자의 북마크만 보이자
            # user -> profile -> bookmark
            profile = Profile.objects.get(user=user)    # user -> profile
            bookmark_list = Bookmark.objects.filter(profile=profile)    # profile -> bookmark_list
        else: # 로그인 안하면 북마크 보이지 말자
            bookmark_list = Bookmark.objects.none()
        return bookmark_list

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['profile', 'name', 'url']
    template_name_suffix = '_create'
    success_url = reverse_lazy('bookmark:list')

    def get_initial(self):
        # user -> profile
        user = self.request.user
        profile = Profile.objects.get(user=user)
        return {'profile': profile}

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