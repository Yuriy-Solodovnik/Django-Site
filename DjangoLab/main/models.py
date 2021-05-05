from django.db import models


class Message(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    body = models.TextField('Тело сообщения')
    date = models.DateField('Дата сообщения')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
