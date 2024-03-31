from django.db import models


# Create your models here.


class MyModel(models.Model):
    name = models.CharField('Название', max_length=100)
    description = models.CharField('Описание', max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.id}'

    class Meta:
        verbose_name = 'Основное'
        verbose_name_plural = 'Основное'
