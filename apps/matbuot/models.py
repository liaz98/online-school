from django.db import models
from django.urls import reverse


class Kategoriya(models.Model):
    title = models.CharField(max_length=150, verbose_name='Sarlavha')
    slug = models.SlugField(max_length=150, verbose_name='Havola')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("yangilik_kategoriya", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Yangilik  kategoriyai'
        verbose_name_plural = '1. Yangilik kategoriyalari'
        ordering = ['title']


class Yangiliklar(models.Model):
    title = models.CharField(max_length=150, verbose_name='Sarlavha')
    slug = models.SlugField(max_length=150, verbose_name='Havola')
    content = models.TextField(verbose_name='Matn')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Joylangan vaqti')
    updated = models.DateTimeField(auto_now=True, verbose_name='Yangilangan vaqti')
    photo = models.ImageField(upload_to='yangiliklar/%y/%m/%d', verbose_name='Surat', blank=True)
    published = models.BooleanField(verbose_name='Yuklangan', default=True)
    category = models.ForeignKey(Kategoriya, on_delete=models.PROTECT, verbose_name='Kategoriyasi')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("yangilik_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Yangilik'
        verbose_name_plural = '1.1 Yangiliklar'
        ordering = ['title']


class Category(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to="image/")
    is_active = models.BooleanField(default=True)
    sortings = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name='Joylashuv')

    objects = models.Manager()

    def __str__(self):
        return f"{self.title}"

    # def get_absolute_url(self):
    #     from django.urls import reverse
    #     return reverse('gallery', args=[str(self.title)])

    class Meta:
        verbose_name = 'Galereya Kategoriyasi'
        verbose_name_plural = '2. Galereya Kategoriyalari'
        ordering = ['sortings']


class CategoryImage(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="image/")
    sortings = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name='Joylashuv')

    objects = models.Manager()

    def __str__(self):
        return f"{self.category}"
        # return "{} -> {}".format(self.category.title, self.image.url)

    class Meta:
        verbose_name = 'Galereya surati'
        verbose_name_plural = '2.1 Galereya suratlari'
        ordering = ['sortings']


class OMV(models.Model):
    title = models.CharField(max_length=150, verbose_name='Sarlavha')
    slug = models.SlugField(max_length=150, verbose_name='Havola')
    content = models.TextField(verbose_name='Matn')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Joylangan vaqti')
    updated = models.DateTimeField(auto_now=True, verbose_name='O`zgartirilgan vaqti')
    photo = models.ImageField(upload_to='yangiliklar/%y/%m/%d', verbose_name='Surat', blank=True)
    published = models.BooleanField(verbose_name='Yuklangan', default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("omv_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name ='OMV biz haqimizda'
        verbose_name_plural = '3. OMV biz haqimizda'
