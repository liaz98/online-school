# Generated by Django 3.1 on 2020-09-15 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Normativ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, verbose_name='Sarlavha')),
                ('slug', models.SlugField(verbose_name='Havola')),
                ('content', models.TextField(verbose_name='O`zb. Davlat normativlari matni')),
            ],
            options={
                'verbose_name': 'Normativ',
                'verbose_name_plural': 'Normativlar',
                'ordering': ['title'],
            },
        ),
    ]
