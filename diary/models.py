from django.db import models

from users.models import User


class Note(models.Model):

    title = models.CharField(max_length=80, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Контент")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время обновления")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")

    def __str__(self):
        return f"{self.title}, {self.created_at}"

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
