# Generated by Django 3.1 on 2020-12-11 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('togaraklar', '0009_auto_20201104_0809'),
    ]

    operations = [
        migrations.CreateModel(
            name='QoshimchaDarsList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Qoshimcha dars nomi')),
                ('slug', models.SlugField(verbose_name='Ilova nomi')),
                ('content', models.TextField(verbose_name='Qoshimcha dars haqida ma`lumot')),
                ('rasm1', models.ImageField(blank=True, null=True, upload_to='qoshimchadars/%m', verbose_name='Bitinchi Rasm')),
                ('rasm2', models.ImageField(blank=True, null=True, upload_to='qoshimchadars/%m', verbose_name='Ikkinchi Rasm')),
                ('rasm3', models.ImageField(blank=True, null=True, upload_to='qoshimchadars/%m', verbose_name='Uchinchi Rasm')),
                ('rasm4', models.ImageField(blank=True, null=True, upload_to='qoshimchadars/%m', verbose_name='To`rtinchi Rasm')),
            ],
            options={
                'verbose_name': 'Qoshimcha dars',
                'verbose_name_plural': 'Qoshimcha darslar',
            },
        ),
    ]
