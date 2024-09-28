from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    fulltext = models.TextField('Содержание')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return f'Новость:{self.title}'
    def get_absolute_url(self):
        return f'/news/{self.id}'
    class Meta:
        verbose_name='Новость'
        verbose_name_plural='Новости'