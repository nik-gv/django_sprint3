"""Импортируем модули."""
from django.shortcuts import get_object_or_404, render

from blog.models import Post, Category


def index(request):
    """View функция для главной страницы."""
    post_list = Post.objects.pub_objects()[:5]
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    """View функция для поста."""
    post = get_object_or_404(
        Post.objects.pub_objects(),
        id=post_id
    )

    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    """View функция для страницы категорий."""
    category = get_object_or_404(Category, slug=category_slug, is_published=True)
    post_list = Post.objects.pub_objects().filter(category=category)
    context = {
        'category': category,
        'post_list': post_list,
    }

    return render(request, 'blog/category.html', context)
