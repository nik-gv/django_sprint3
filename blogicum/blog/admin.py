from django.contrib import admin

from .models import Category, Location, Post


class PostInline(admin.StackedInline):
    model = Post
    extra = 3


class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        PostInline,
    )
    list_display = (
        'title',
        'description',
        'slug',
        'is_published'
    )
    list_editable = (
        'description',
        'slug',
        'is_published'
    )


class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'is_published', 

    )
    list_editable = (
        'is_published',
    )


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'text',
    )
    list_editable = (
        'text',
    )

    search_fields = ('title',)
    list_filter = ('category',)
    list_display_links = ('title',)
    empty_value_display = 'Не задано'

admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Post, PostAdmin)