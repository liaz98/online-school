from django.db import models
from django.urls import reverse
# Create your models here.


class ChildrenBook(models.Model):
    link = models.URLField(verbose_name="web site manzili")
    public_link = models.CharField(max_length=64, verbose_name="web site", default="tegilmasin-yozilmasin")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.link}"

    def save(self, *args, **kwargs):
        full_link = self.link
        remove_protocol = ""
        if self.public_link == "tegilmasin-yozilmasin" or "":
            if "https://www" in full_link:
                remove_protocol += self.link.replace("https://www", "")
            elif "http://www" in full_link:
                remove_protocol += self.link.replace("http://www", "")
            elif "https://" in full_link:
                remove_protocol += self.link.replace("https://", "")
            elif "http://" in full_link:
                remove_protocol += self.link.replace("http://", "")
            else:
                remove_protocol += self.link
        else:
            remove_protocol += self.link
        self.public_link = remove_protocol
        super(ChildrenBook, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Maktab kutubxonasi'
        verbose_name_plural = '1. Maktab kutubxonasi'

class TableBook(models.Model):
    name = models.CharField(max_length=150, verbose_name="Kitobning nomi")
    author = models.CharField(max_length=150, verbose_name="Kitobning mualifi")
    language = models.CharField(max_length=150, verbose_name="Kitobning matni")

    class Meta:
        verbose_name = 'Kitoblar ro`yxati.'
        verbose_name_plural = '1.1 Kitoblar ro`yxati.'

class Electron(models.Model):
    title = models.CharField(max_length=150, verbose_name='Sarlavha')
    slug = models.SlugField(max_length=150, verbose_name='Havola')
    content = models.TextField(verbose_name='Matn')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Joylangan vaqti')
    updated = models.DateTimeField(auto_now=True, verbose_name='Yangilangan vaqti')
    photo = models.ImageField(upload_to='yangiliklar/%y/%m/%d', verbose_name='Dars Surat', blank=True)
    published = models.BooleanField(verbose_name='Yuklangan', default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("electron_detail", kwargs={"slug": self.slug})


class Video(models.Model):
    title = models.CharField(max_length=150, verbose_name='Sarlavha')
    slug = models.SlugField(max_length=150, verbose_name='Havola')
    content = models.TextField(verbose_name='Matn')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Joylangan vaqti')
    updated = models.DateTimeField(auto_now=True, verbose_name='Yangilangan vaqti')
    photo = models.ImageField(upload_to='yangiliklar/%y/%m/%d', verbose_name='Dars Surat', blank=True)
    published = models.BooleanField(verbose_name='Yuklangan', default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("video_detail", kwargs={"slug": self.slug})