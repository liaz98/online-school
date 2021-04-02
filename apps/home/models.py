from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse


class Aloqa(models.Model):
    adress = models.TextField(verbose_name='Manzil')
    phone = PhoneNumberField(max_length=13, verbose_name='Telefon')
    second_phone = PhoneNumberField(max_length=13, blank=True, verbose_name='Ikkinchi telefon (agar bolsa)')
    email = models.EmailField(verbose_name='Email')
    map = models.TextField(verbose_name='Karta')

    def __str__(self):
        return f"{self.adress}"

    class Meta:
        verbose_name = 'Aloqa'
        verbose_name_plural = '3. Aloqa'


class Savollar(models.Model):
    savol = models.TextField(verbose_name='Savol matni')
    javob = models.TextField(verbose_name='Javob matni')

    def __str__(self):
        return self.savol

    class Meta:
        verbose_name = 'Savol va Javob'
        verbose_name_plural = '1. Savollar va Javoblar'


class FatherAndMother(models.Model):
    title = models.CharField(max_length=150, verbose_name='Sarlavha')
    slug = models.SlugField(max_length=150, verbose_name='Havola')
    content = models.TextField(verbose_name='Matn')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Joylangan vaqti')
    updated = models.DateTimeField(auto_now=True, verbose_name='Yangilangan vaqti')
    photo = models.ImageField(upload_to='yangiliklar/%y/%m/%d', verbose_name='OtaOna Surat', blank=True)
    published = models.BooleanField(verbose_name='Yuklangan', default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("fm_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Ota-onalarga'
        verbose_name_plural = '2. Ota-onalarga'


class Reklama(models.Model):
    image = models.ImageField(upload_to='reklamalar', blank=True)
    link = models.CharField(max_length=150,blank=True)


    class Meta:
        verbose_name = 'Reklama'
        verbose_name_plural = '4. Reklamalar'



