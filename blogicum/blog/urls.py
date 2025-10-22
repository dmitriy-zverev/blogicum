from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='index'),
    path(
        'add_comment/<int:id>',
        views.PostListView.as_view(),
        name='add_comment',
    ),
    path(
        'create/',
        views.PostCreateView.as_view(),
        name='create',
    ),
    path(
        'category/<slug:category_slug>/',
        views.CategoryListView.as_view(),
        name='category_posts',
    ),
    path(
        'delete/<int:pk>',
        views.PostDeleteView.as_view(),
        name='delete_post',
    ),
    path(
        'edit/<int:pk>',
        views.PostUpdateView.as_view(),
        name='edit_post',
    ),
    path(
        'edit_profile/',
        views.ProfileEditView.as_view(),
        name='edit_profile',
    ),
    path(
        'posts/<int:pk>/',
        views.PostDetailView.as_view(),
        name='post_detail',
    ),
    path(
        'posts/<int:pk>/edit/',
        views.PostEditView.as_view(),
        name='edit_post',
    ),
    path(
        'profile/<slug:username>/',
        views.ProfileListView.as_view(),
        name='profile',
    ),
    path(
        'password_change/',
        auth_views.PasswordChangeView.as_view(
            template_name='registration/password_change_form.html'),
        name='password_change',
    ),
    path(
        'password_change/done/',
        auth_views.PasswordChangeDoneView.as_view(
            template_name='registration/password_change_done.html'),
        name='password_change_done',
    ),
]
