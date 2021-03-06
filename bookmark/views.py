from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from accounts.models import Profile
from bookmark.forms import BookmarkCreationForm, BookmarkChangeForm
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
            # bookmark_list = Bookmark.objects.all()
            bookmark_list = Bookmark.objects.none()
        return bookmark_list

class BookmarkCreateView(LoginRequiredMixin, CreateView):
    model = Bookmark
    fields = ['profile', 'name', 'url']
    template_name_suffix = '_create'
    success_url = reverse_lazy('bookmark:list')

    def get_initial(self):
        # user -> profile
        user = self.request.user
        profile = Profile.objects.get(user=user)
        return {'profile': profile}

class BookmarkDetailView(LoginRequiredMixin, DetailView):
    model = Bookmark

class BookmarkUpdateView(LoginRequiredMixin, UpdateView):
    model = Bookmark
    fields = ['name', 'url']
    template_name_suffix = '_update'
    # success_url = reverse_lazy('bookmark:list')

class BookmarkDeleteView(LoginRequiredMixin, DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:list')

def list_bookmark(request):
    # 로그인 사용자 확인하자
    user = request.user
    if user.is_authenticated: #로그인 되어있으면
        profile = Profile.objects.get(user=user)
        bookmark_list = Bookmark.objects.filter(profile=profile) # 그 사용자의 북마크 가져오자
    else: # 로그인 안 되어 있으면
        bookmark_list = Bookmark.objects.none() # 북마크 없는 것 가져오자

    return render(request, 'bookmark/bookmark_list.html', {'bookmark_list': bookmark_list})

def detail_bookmark(request, pk):
    bookmark = Bookmark.objects.get(pk=pk)
    return render(request, 'bookmark/bookmark_detail.html', {'bookmark': bookmark})

def delete_bookmark(request, pk):
    if request.method == 'POST':    # 삭제 버튼 눌렀을 때
        bookmark = Bookmark.objects.get(pk=pk)
        bookmark.delete()
        return redirect('bookmark:list')
    else:   # 처음 bookmark_delete.html 요청
        bookmark = Bookmark.objects.get(pk=pk)
        return render(request, 'bookmark/bookmark_confirm_delete.html', {'bookmark': bookmark})

@login_required
def create_bookmark(request):
    if request.method == 'POST':    #사용자가 입력하고 버튼 눌렀을 때
        form = BookmarkCreationForm(request.POST)   #form 가져오자
        if form.is_valid(): #is_valid()
            new_bookmark = form.save(commit=False)  #new_bookmark 생성하자(name, url)
            new_bookmark.profile = Profile.objects.get(user=request.user)   #new_bookmark에 profile 추가하자
            new_bookmark.save()
            return redirect('bookmark:list')  #bookmark:list 이동하자
    else:   #빈 폼
        form = BookmarkCreationForm()
    return render(request, 'bookmark/bookmark_create.html', {'form': form})

@login_required
def modify_bookmark(request, pk):
    if request.method == 'POST':
        form = BookmarkChangeForm(request.POST)     # form 가져오자
        if form.is_valid(): # is_valid()
            bookmark = Bookmark.objects.get(pk=pk)  # pk에 해당하는 bookmark 가져오자
            bookmark.name = form.cleaned_data.get('name')   # 사용자가 입력한 name set
            bookmark.url = form.cleaned_data.get('url') # 사용자가 입력한 url set
            bookmark.save()
            return redirect('bookmark:list')    # bookmark:list로 이동하자
    else:
        bookmark = Bookmark.objects.get(pk=pk)  # pk에 해당하는 bookmark 정보 가져오자
        form = BookmarkChangeForm(instance=bookmark)    # bookmark 정보 넣은 form
    return render(request, 'bookmark/bookmark_update.html', {'form': form})