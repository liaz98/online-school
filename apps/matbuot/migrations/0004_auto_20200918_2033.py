# Generated by Django 3.1 on 2020-09-18 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matbuot', '0003_auto_20200918_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galereya',
            name='image',
            field=models.ImageField(upload_to='galereya/', verbose_name='Suratni joylang'),
        ),
    ]