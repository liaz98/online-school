# Generated by Django 3.1 on 2020-12-16 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qonun', '0005_auto_20201118_1125'),
    ]

    operations = [
        migrations.CreateModel(
            name='Qoidalar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sarlavha', models.TextField(verbose_name='Qoida sarlavhasi')),
                ('slug', models.SlugField(verbose_name='Havola')),
                ('matni', models.TextField(verbose_name='Qoida matni')),
            ],
            options={
                'verbose_name': 'Maktab qoidalari',
                'verbose_name_plural': 'Maktab qoidalari',
                'ordering': ['sarlavha'],
            },
        ),
        migrations.DeleteModel(
            name='Maktab_Qoidalari',
        ),
    ]
