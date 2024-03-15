from django.contrib import admin
from users.models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "author",
        "content",
        "created",
    ]
