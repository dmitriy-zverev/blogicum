from datetime import datetime
from django.shortcuts import get_object_or_404, reverse
from django.db.models import Count
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import Post, Category, Comment
from .forms import PostForm, CommentForm
from users.forms import CustomUserChangeForm

User = get_user_model()


class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    queryset = Post.objects.select_related(
        'location',
        'category',
        'author',
    ).filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=datetime.now(),
    ).annotate(comment_count=Count('comments'))
    ordering = '-pub_date'
    paginate_by = 20


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    queryset = Post.objects.select_related(
        'location',
        'category',
        'author',
    ).filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=datetime.now(),
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['comments'] = (self.object.comments.select_related('author'))
        return context


class CategoryListView(ListView):
    model = Post
    template_name = 'blog/category.html'
    paginate_by = 20

    def dispatch(self, request, *args, **kwargs):
        self.category_slug = kwargs.get('category_slug')
        self.category = get_object_or_404(
            Category,
            slug=self.category_slug,
            is_published=True,
        )
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return Post.objects.select_related(
            'category',
            'location',
            'author',
        ).filter(
            category__slug=self.category_slug,
            is_published=True,
            pub_date__lte=datetime.now(),
        ).annotate(comment_count=Count('comments')).order_by('-pub_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        context['page_obj'] = self.get_queryset()
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/create.html'
    success_url = reverse_lazy('blog:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/create.html'
    success_url = reverse_lazy('blog:index')

    def dispatch(self, request, *args, **kwargs):
        get_object_or_404(
            Post,
            pk=kwargs['pk'],
            author=request.user,
        )
        return super().dispatch(request, *args, **kwargs)


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/create.html'
    success_url = reverse_lazy('blog:index')

    def dispatch(self, request, *args, **kwargs):
        self.post_obj = get_object_or_404(
            Post,
            pk=kwargs['pk'],
            author=request.user,
        )
        if self.post_obj.author != request.user:
            return redirect('blog:post_detail', pk=self.post_obj.pk)
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return self.post_obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = self.post_obj
        return context


class PostEditView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/create.html'

    def dispatch(self, request, *args, **kwargs):
        post = get_object_or_404(
            Post,
            pk=kwargs['pk'],
            author=request.user,
        )
        if post.author != request.user:
            return redirect('blog:post_detail', pk=post.pk)
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse(
            'blog:post_detail',
            kwargs={'pk': self.object.pk},
        )


class ProfileListView(ListView):
    model = Post
    slug_field = 'username'
    slug_url_kwarg = 'username'
    template_name = 'blog/profile.html'
    paginate_by = 20

    def dispatch(self, request, *args, **kwargs):
        self.username = kwargs.get('username')
        self.profile = get_object_or_404(
            User,
            username=self.username,
        )
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return Post.objects.select_related(
            'location',
            'category',
            'author',
        ).filter(author=self.profile, ).annotate(
            comment_count=Count('comments')).order_by('-pub_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.profile
        return context


class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name = 'blog/user.html'

    def dispatch(self, request, *args, **kwargs):
        self.username = request.user
        self.profile = get_object_or_404(
            User,
            username=self.username,
        )
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def get_success_url(self):
        return reverse(
            'blog:profile',
            kwargs={'username': self.username},
        )


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment.html'

    def dispatch(self, request, *args, **kwargs):
        self.post_obj = get_object_or_404(Post, pk=kwargs['post_id'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = self.post_obj
        return super().form_valid(form)

    def get_success_url(self):
        return reverse(
            'blog:post_detail',
            kwargs={'pk': self.post_obj.pk},
        )


class CommentEditView(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment.html'

    def dispatch(self, request, *args, **kwargs):
        self.comment = get_object_or_404(
            Comment,
            pk=kwargs['comment_id'],
            author=request.user,
        )
        if self.comment.author != request.user:
            return redirect('blog:post_detail', pk=self.comment.post_id)
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return self.comment

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment'] = self.comment
        return context

    def get_success_url(self):
        return reverse(
            'blog:post_detail',
            kwargs={'pk': self.comment.post_id},
        )


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment.html'

    def dispatch(self, request, *args, **kwargs):
        self.comment = get_object_or_404(
            Comment,
            pk=kwargs['comment_id'],
            author=request.user,
        )
        if self.comment.author != request.user:
            return redirect('blog:post_detail', pk=self.comment.post_id)
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return self.comment

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        context['comment'] = self.comment
        return context

    def get_success_url(self):
        return reverse(
            'blog:post_detail',
            kwargs={'pk': self.comment.post_id},
        )
