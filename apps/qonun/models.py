from django.db import models


class Normativ(models.Model):
    title = models.TextField(verbose_name='Sarlavha', blank=True)
    slug = models.SlugField(max_length=50, verbose_name='Havola')
    content = models.TextField(verbose_name='O`zb. Davlat normativlari matni')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Normativ'
        verbose_name_plural = '2. O`zbekiston davlat Normativlari'
        ordering = ['title']

    def __str__(self):
        return self.title

class Qoidalar(models.Model):
    sarlavha = models.TextField(verbose_name='Qoida sarlavhasi')
    matni = models.TextField(verbose_name='Qoida matni')

    def __str__(self):
        return self.sarlavha

    class Meta:
        verbose_name = 'Maktab qoidalari'
        verbose_name_plural = '1. Maktab qoidalari'
        ordering = ['sarlavha']
