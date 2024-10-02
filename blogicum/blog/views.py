"""Импортируем модуль http404."""
from django.http import Http404
from django.shortcuts import render
from blog.models import Post, Category
from django.utils import timezone


def index(request):
    """View функция для главной страницы."""
    post_list = Post.objects.all().filter(
        pub_date__lt=timezone.now(),
        is_published=True,
        category__is_published=True).order_by('-created_at')[:5]
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    """View функция для поста."""
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404(f"Страница {post_id} не найдена")
    if (not post.is_published or
            not post.category.is_published or
            post.pub_date >= timezone.now()):
        raise Http404(f"Страница {post_id} не найдена")

    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    """View функция для страницы категорий."""
    try:
        category = Category.objects.get(slug=category_slug, is_published=True)
    except Category.DoesNotExist:
        raise Http404(f"Категория '{category_slug}' не найдена")
    post_list = Post.objects.filter(
        category=category,
        is_published=True,
        pub_date__lt=timezone.now()).order_by('-created_at')
    context = {
        'category': category,  # Передаем объект категории
        'post_list': post_list,  # Передаем список постов в категории
    }
    return render(request, 'blog/category.html', context)
