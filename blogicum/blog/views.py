from django.http import Http404
from django.shortcuts import render
from blog.models import Post, Category
from datetime import datetime
from django.utils import timezone

posts = [
    {
        'id': 0,
        'location': 'Остров отчаянья',
        'date': '30 сентября 1659 года',
        'category': 'travel',
        'text': '''Наш корабль, застигнутый в открытом море
                страшным штормом, потерпел крушение.
                Весь экипаж, кроме меня, утонул; я же,
                несчастный Робинзон Крузо, был выброшен
                полумёртвым на берег этого проклятого острова,
                который назвал островом Отчаяния.''',
    },
    {
        'id': 1,
        'location': 'Остров отчаянья',
        'date': '1 октября 1659 года',
        'category': 'not-my-day',
        'text': '''Проснувшись поутру, я увидел, что наш корабль сняло
                с мели приливом и пригнало гораздо ближе к берегу.
                Это подало мне надежду, что, когда ветер стихнет,
                мне удастся добраться до корабля и запастись едой и
                другими необходимыми вещами. Я немного приободрился,
                хотя печаль о погибших товарищах не покидала меня.
                Мне всё думалось, что, останься мы на корабле, мы
                непременно спаслись бы. Теперь из его обломков мы могли бы
                построить баркас, на котором и выбрались бы из этого
                гиблого места.''',
    },
    {
        'id': 2,
        'location': 'Остров отчаянья',
        'date': '25 октября 1659 года',
        'category': 'not-my-day',
        'text': '''Всю ночь и весь день шёл дождь и дул сильный
                порывистый ветер. 25 октября.  Корабль за ночь разбило
                в щепки; на том месте, где он стоял, торчат какие-то
                жалкие обломки,  да и те видны только во время отлива.
                Весь этот день я хлопотал  около вещей: укрывал и
                укутывал их, чтобы не испортились от дождя.''',
    },
]
posts_dic = {d['id']: d for d in posts}


def index(request):
    """View функция для главной страницы."""
    post_list = Post.objects.all().filter(pub_date__lt=timezone.now(), is_published=True, category__is_published=True).order_by('-created_at')[:5]
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    """View функция для поста."""
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404(f"Страница {post_id} не найдена")
    if not post.is_published or not post.category.is_published or post.pub_date >= timezone.now():
        raise Http404(f"Страница {post_id} не найдена")
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    """View функция для страницы категорий."""
    try:
        category = Category.objects.get(slug=category_slug, is_published=True)
    except Category.DoesNotExist:
        raise Http404(f"Категория '{category_slug}' не найдена")
    post_list = Post.objects.filter(category=category, is_published=True, pub_date__lt=timezone.now()).order_by('-created_at')
    context = {
        'category': category,  # Передаем объект категории
        'post_list': post_list,  # Передаем список постов в категории
    }
    return render(request, 'blog/category.html', context)
