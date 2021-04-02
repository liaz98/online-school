from django.db import models
from django.urls import reverse


class Kategoriya(models.Model):
    title = models.CharField(max_length=150, verbose_name='Sinf kategoriyasi')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='Havola')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Sinf kategoriyasi'
        verbose_name_plural = '1. Sinf kategoriyalari'
        ordering = ['title']


class Teacher(models.Model):
    teacher_name = models.CharField(max_length=60, verbose_name='O`qituvchi ismi')
    teacher_position = models.CharField(max_length=60, verbose_name='O`qituvchi lavozimi')
    teacher_photo = models.ImageField(upload_to='oqituvchilar/', verbose_name='O`qituvchi surati')
    sortings = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name='Joylashuv')

    class Meta:
        verbose_name = 'O`qituvchi'
        verbose_name_plural = '5. O`qituvchilar'
        ordering = ['sortings']

    def __str__(self):
        return self.teacher_name


class Sinf(models.Model):
    title = models.CharField(max_length=150, verbose_name='Sinf nomi')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='Havola')
    content = models.TextField(blank=True, verbose_name='Sinf haqida qisqacha ma`lumot')
    school_photo = models.ImageField(upload_to='sinflar_rasmi/', verbose_name='Sinf surati', blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')
    updated = models.DateTimeField(auto_now=True, verbose_name='Oxirgi yangilan vaqti')
    published = models.BooleanField(verbose_name='Sitega qo`yilgan', default=True)
    school_teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT, verbose_name='O`qituvchi', null=True,
                                       related_name="sinflar")
    school_news = models.ForeignKey(Kategoriya, on_delete=models.PROTECT, verbose_name='Maktab')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("sinf_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Sinf'
        verbose_name_plural = '1.1 Sinflar'
        ordering = ['title']


class Yangiliklar(models.Model):
    title = models.CharField(max_length=150, verbose_name='Sarlavha')
    slug = models.SlugField(max_length=150, verbose_name='Havola')
    content = models.TextField(verbose_name='Matn')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Joylangan vaqti')
    updated = models.DateTimeField(auto_now=True, verbose_name='Yangilangan vaqti')
    published = models.BooleanField(verbose_name='Yuklangan', default=True)
    category = models.ForeignKey(Kategoriya, on_delete=models.PROTECT, verbose_name='Sinf')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("sinf_yangilik_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Sinf Yangilik'
        verbose_name_plural = '1.2 Sinf Yangiliklari'
        ordering = ['title']


class DarsJadvali(models.Model):
    date = models.DateField(verbose_name='Jadal joylangan sana')
    jadval = models.ImageField(upload_to='dars_jadvallari/')

    class Meta:
        verbose_name = 'Jadval'
        verbose_name_plural = '3. Asosiy darslar'


class KunTartibi(models.Model):
    start_time = models.TimeField(verbose_name='Boshlanish vaqti. Masalan: 08:45')
    end_time = models.TimeField(verbose_name='Tugash vaqti. Masalan: 12:45')
    title = models.CharField(max_length=200, verbose_name='Sarlavha')
    content = models.TextField(verbose_name='Matn')
    created = models.DateTimeField(auto_now=True, verbose_name='Saytga qo`yilgan vaqti')
    sortings = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name='Joylashuv')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['sortings']
        verbose_name = 'Kun Tartibi'
        verbose_name_plural = '2. Kun tartibi'


class KitchenContent(models.Model):
    title = models.CharField(max_length=20, verbose_name='Oshxona sarlavhasi')
    kitchen_text = models.TextField(blank=True, verbose_name='Oshxona texti')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Oshxona'
        verbose_name_plural = '6. Oshxona'


# oshxona gallereyasi
class ImageGallery(models.Model):
    title = models.CharField(max_length=50, blank=True, verbose_name='Sarlavha')
    pictures = models.ImageField(upload_to='oshxona/', verbose_name='Rasm joylashtiring ')
    content = models.ForeignKey(KitchenContent, blank=True, on_delete=models.CASCADE,
                                related_name='%(class)s_requests_created', default=None)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ' Rasmlar '
        verbose_name_plural = ' Rasmlar '


class Kitchen(models.Model):
    image = models.ImageField(upload_to='kitchen/', verbose_name='Rasm joylashtiring')
    date = models.DateField(verbose_name='Joylangan sana')
    content = models.ForeignKey(KitchenContent, blank=True, on_delete=models.CASCADE,
                                related_name='%(class)s_requests_created', default=None)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('kitchen_detail', args=[int(self.pk)])

    def __str__(self):
        return f"{self.date}"

    class Meta:
        verbose_name = 'Taomnoma '
        verbose_name_plural = 'Taomnoma '


class ChoyContent(models.Model):
    title = models.CharField(max_length=20, verbose_name='Tolmas choy sarlavhasi')
    choy_text = models.TextField(blank=True, verbose_name='Matn')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ' Tolmas choy'
        verbose_name_plural = '6.1 Tolmas Choy'


class Choy(models.Model):
    date = models.DateField(verbose_name='Joylangan sana')
    image = models.ImageField(upload_to='kitchen/choy', verbose_name='Rasm')
    content = models.ForeignKey(ChoyContent, blank=True, on_delete=models.CASCADE,
                                related_name='%(class)s_requests_created', default=None)

    def get_absolute_url(self):
        return reverse('choy_detail', args=[int(self.pk)])

    def __str__(self):
        return f"{self.date}"

    class Meta:
        verbose_name = ' Tolmas choy'
        verbose_name_plural = ' Tolmas Choy'


class ImageCollection(models.Model):
    title = models.CharField(max_length=50, blank=True, verbose_name='Sarlavha')
    image = models.ImageField(upload_to='choy/', verbose_name='Rasm')
    content = models.ForeignKey(ChoyContent, blank=True, on_delete=models.CASCADE,
                                related_name='%(class)s_requests_created', default=None)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ' Rasmlar '
        verbose_name_plural = ' Rasmlar '


class Jarayon(models.Model):
    title = models.CharField(max_length=150, verbose_name='Sarlavha')
    slug = models.SlugField(max_length=150, verbose_name='Havola')
    content = models.TextField(verbose_name='Matn')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Joylangan vaqti')
    updated = models.DateTimeField(auto_now=True, verbose_name='Yangilangan vaqti')
    photo = models.ImageField(upload_to='yangiliklar/%y/%m/%d', verbose_name='Jarayon Surat', blank=True)
    published = models.BooleanField(verbose_name='Yuklangan', default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("jarayon_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Jarayon'
        verbose_name_plural = '4. O`quv Jarayoni'
