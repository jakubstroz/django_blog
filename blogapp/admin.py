from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'status',
        'created_by',
        'create_date',
        'update_date',
        'publish_date',
    )

    list_filter = (
        'status',
        'created_by',
        'create_date',
        'update_date',
        'publish_date',
    )

    search_fields = (
        'status',
        'title',
        'body',
        'created_by',
    )

    prepopulated_fields = {'slug':('title',)}