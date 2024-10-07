"""Импортируем модули."""
from django.db import models
from core.models import PublishedModel
from django.contrib.auth import get_user_model
from django.utils import timezone


class PublishedPosts(models.Manager):
    """Менеджер модели."""

    def pub_objects(self):
        """Фильтр."""
        return self.filter(
            pub_date__lte=timezone.now(),
            is_published=True,
            category__is_published=True
        ).order_by('-created_at')


class Category(PublishedModel):
    """Модель категории для публикаций."""

    title = models.CharField(max_length=256, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(
        unique=True,
        verbose_name='Идентификатор',
        help_text=('Идентификатор страницы для URL; '
                   'разрешены символы латиницы, цифры, дефис и подчёркивание.')
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Добавлено'
    )

    class Meta:
        """Meta данные модели."""

        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        """Возвращает строковое представление категории."""
        return self.title


class Location(PublishedModel):
    """Модель местоположения для публикаций."""

    name = models.CharField(max_length=256, verbose_name='Название места')
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Добавлено'
    )

    class Meta:
        """Meta данные модели."""

        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        """Возвращает строковое представление местоположения."""
        return self.name


User = get_user_model()


class Post(PublishedModel):
    """Модель публикации."""

    title = models.CharField(max_length=256, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(
        verbose_name='Дата и время публикации',
        help_text=('Если установить дату и время в будущем — '
                   'можно делать отложенные публикации.')
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор публикации'
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Местоположение'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Категория'
    )
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Добавлено')
    objects = PublishedPosts()

    class Meta:
        """Meta данные модели."""

        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        """Возвращает строковое представление публикации."""
        return self.title
