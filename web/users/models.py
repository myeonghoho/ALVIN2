from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField("제목", default=None, null=True, max_length=100)
    content = models.TextField("내용", blank=True)
    author = models.CharField("작성자", default=None, null=True, max_length=30)
    created = models.DateTimeField("작성일시", auto_now_add=True)
    

    def __str__ (self):
        return f"Post(id: {self.id})"
