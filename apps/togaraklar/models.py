from django.db import models
from django.urls import reverse


class TogarakList(models.Model):
    title = models.CharField(max_length=150, verbose_name='To`garak nomi')
    slug = models.SlugField(max_length=50, verbose_name='Ilova')
    content = models.TextField(verbose_name='To`garak haqida ma`lumot')
    rasm1 = models.ImageField(upload_to='togarak/%m', verbose_name='Bitinchi Rasm', null=True, blank=True)
    rasm2 = models.ImageField(upload_to='togarak/%m', verbose_name='Ikkinchi Rasm', null=True, blank=True)
    rasm3 = models.ImageField(upload_to='togarak/%m', verbose_name='Uchinchi Rasm', null=True, blank=True)
    rasm4 = models.ImageField(upload_to='togarak/%m', verbose_name='To`rtinchi Rasm', null=True, blank=True)
    videofile1 = models.FileField(upload_to='togarak/videos/', null=True, verbose_name="Video 1", blank=True)
    videofile2 = models.FileField(upload_to='togarak/videos/', null=True, verbose_name="Video 2", blank=True)
    videofile3 = models.FileField(upload_to='togarak/videos/', null=True, verbose_name="Video 3", blank=True)
    videofile4 = models.FileField(upload_to='togarak/videos/', null=True, verbose_name="Video 4", blank=True)

    def get_absolute_url(self):
        return reverse('togarak_detail', kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'To`garak'
        verbose_name_plural = '2. To`garaklar'


class QoshimchaDarsList(models.Model):
    title = models.CharField(max_length=150, verbose_name='Qoshimcha dars nomi')
    slug = models.SlugField(max_length=50, verbose_name='Ilova nomi')
    content = models.TextField(verbose_name='Qoshimcha dars haqida ma`lumot')
    rasm1 = models.ImageField(upload_to='qoshimchadars/%m', verbose_name='Bitinchi Rasm', null=True, blank=True)
    rasm2 = models.ImageField(upload_to='qoshimchadars/%m', verbose_name='Ikkinchi Rasm', null=True, blank=True)
    rasm3 = models.ImageField(upload_to='qoshimchadars/%m', verbose_name='Uchinchi Rasm', null=True, blank=True)
    rasm4 = models.ImageField(upload_to='qoshimchadars/%m', verbose_name='To`rtinchi Rasm', null=True, blank=True)
    videofile1 = models.FileField(upload_to='qoshimchadars/videos/', null=True, verbose_name="Video 1", blank=True)
    videofile2 = models.FileField(upload_to='qoshimchadars/videos/', null=True, verbose_name="Video 2", blank=True)
    videofile3 = models.FileField(upload_to='qoshimchadars/videos/', null=True, verbose_name="Video 3", blank=True)
    videofile4 = models.FileField(upload_to='qoshimchadars/videos/', null=True, verbose_name="Video 4", blank=True)

    def get_absolute_url(self):
        return reverse('qoshimchadars_detail', kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Qoshimcha dars'
        verbose_name_plural = '1. Qo`shimcha darslar'
