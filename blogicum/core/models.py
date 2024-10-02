"""Импортируем модуль models."""
from django.db import models


class PublishedModel(models.Model):
    """Создаем абстрактную модель."""

    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.'
        )

    class Meta:
        """Создаем абстрактную модель."""

        abstract = True
