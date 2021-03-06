# Generated by Django 3.1 on 2020-09-18 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matbuot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Galereya',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, verbose_name='Suratga sharh agar bolsa')),
                ('image', models.ImageField(upload_to='galereya/', verbose_name='Galereya uchun suratni joylang')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Qo`yilgan vaqti')),
            ],
            options={
                'verbose_name': 'Galereya',
                'verbose_name_plural': 'Galereya',
                'ordering': ['image'],
            },
        ),
    ]
