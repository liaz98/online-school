# Generated by Django 3.1 on 2020-10-24 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kutubxona', '0002_childrenbook_public_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='childrenbook',
            name='public_link',
            field=models.CharField(default='tegilmasin-yozilmasin', max_length=64, verbose_name='web site'),
        ),
    ]