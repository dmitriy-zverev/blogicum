from datetime import datetime
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .models import Post, Category


def index(request):
    template_name = 'blog/index.html'

    current_datetime = datetime.now()

    post_list = Post.objects.select_related('location', 'category',
                                            'author').filter(
                                                is_published=True,
                                                category__is_published=True,
                                                pub_date__lte=current_datetime,
                                            )[:5]

    context = {'post_list': post_list}

    return render(request, template_name, context)


def post_detail(request, id):
    template_name = 'blog/detail.html'

    current_datetime = datetime.now()

    queryset = Post.objects.select_related(
        'category', 'location', 'author').filter(
            Q(is_published=True) & Q(category__is_published=True)
            & Q(pub_date__lte=current_datetime))
    post = get_object_or_404(queryset, id=id)

    context = {'post': post}

    return render(request, template_name, context)


def category_posts(request, category_slug):
    template_name = 'blog/category.html'

    current_datetime = datetime.now()

    category = get_object_or_404(Category,
                                 slug=category_slug,
                                 is_published=True)

    post_list = Post.objects.select_related('category', 'location',
                                            'author').filter(
                                                category__slug=category_slug,
                                                is_published=True,
                                                pub_date__lte=current_datetime,
                                            )

    context = {'post_list': post_list, 'category': category}
    return render(request, template_name, context)
