# DBookmark
- project/urls.py -> app/urls.py -> views.py -> models.py -> templates/app/index.html
- admin.py : 관리자 사이트
- form.py : 입력 사이트
- 개발 순서 : models.py, views.py, urls.py, templates
1. startproject DBookmark
   1. python -m pip install django~=3.2
   2. django-admin startproject DBookmark .
   3. python manage.py runserver
2. startapp bookmark
   1. python manage.py startapp bookmark
   2. add 'bookmark', to INSTALLED_APPS in settings.py
3. bookmark/models.py 
   1. python manage.py makemigrations bookmark
      1. models -> DB로 옮기기 위한 py
   2. python manage.py migrate
      1. DB 테이블 만들기
   3. bookmark/admin Bookmark
      1. python manage.py createsuperuser
      2. bookmark/models Bookmark \_\_str\_\_()
   4. bookmark/views BookmarkListView
   5. urls, bookmark/urls bookmark:list
   6. templates bookmark_list.html
   7. bookmark/views BookmarksCreateView
   8. urls, bookmark/urls bookmark:add
   9. templates bookmark_create.html
   10. bookmark/view BookmarkDetailView
   11. bookmark/urls bookmark:detail
   12. templates bookmark_detail.html
   13. bookmark/views BookmarkUpdateView
   14. bookmark/urls bookmark:edit
   15. templates bookmark_update.html
   16. get_absolute_url() in Bookmark
   17. bookmark/views BookmarkDeleteView
   18. bookmark/urls bookmark:delete
   19. templates bookmark_confirm_delete.html
4. 끝!
   1. templates/base.html, extends 'base.html', block title, content
---
- accounts Profile
  - startapp accounts 
    - python manage.py startapp accounts
    - 'accounts', in INSTALLED_APPS settings
  - accounts/models Profile
    - python manage.py makemigrations accounts
    - python manage.py migrate accounts
  - bookmark/models add prodile in Bookmark
    - python manage.py makemifrations bookmark
      1. 기존에 자료가 있으면 에러남 (다 지우고 다시 하거나)
      2. Bookmark의 profile에 null=True 
      3. python manage.py makemigrations bookmark
    - python manage.py migrate bookmark
      - admin 사이트에서 로그인 후 Profile 하나 추가하고
      - 기존 북마크에 profile 지정하자
  - accounts/admin ProfileAdmin
  - register
    - accounts/forms RegisterForm(UserCreationForm)
    - accounts/views register
    - DBookmark/urls, accounts/urls accounts:register
    - accounts/templates/accounts register, register_done
      - bookmark/ templates/boormark boormark_list
  - login, logout
    - accounts/forms LoginForm
    - accounts/views my_login, my_logout
    - accounts/urls accounts:login, logout
    - accounts/templates/accounts login, login_fail
      - bookmark/templates/bookmark login, logout
    - bookmark/views BookmarkListView get_queryset(), BookmarkCreateView get_initial()
    - bookmark/templates/bookmark bookmark_create profile 숨기자
    - accounts/templates/accounts add login link in register_done
    - 로그인 요구하기
      - FBV: @login_required
        - accounts/views my_logout
      - CBV: (LoginRequiredMixin, )
        - bookmark/view BookmarkCreateView, BookmarkDetailView, BookmarkUpdateView, BookmarkDeleteView
    - 로그인 요구할 때 이동할 URL setting
      - settings LOGIN_URL
    - 로그인 후 REDIRECT_FIELD_NAME으로 이동하자
  - FBV list_bookmark
    - bookmark/views
    - bookmark/urls
    - DBookmark/urls