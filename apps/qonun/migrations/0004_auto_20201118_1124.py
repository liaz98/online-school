# Generated by Django 3.1 on 2020-11-18 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qonun', '0003_maktab_qoidalari'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maktab_qoidalari',
            name='title',
            field=models.CharField(blank=True, max_length=150, verbose_name='Sarlavha'),
        ),
    ]