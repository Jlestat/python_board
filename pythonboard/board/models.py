from django.db import models


class Post(models.Model):
    title = models.CharField(verbose_name='Название объявления', max_length=150)
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
